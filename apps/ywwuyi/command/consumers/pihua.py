import time,datetime
from ywwuyi.cqrequest import send_group_msg, get_group_member_info
from ywwuyi.models.qq_message import QQMessage
from django.db.models import Count

chinese_num = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    10: "十",
}


def parse_msg(result, index):
    msg = ""
    if len(result) > index and int(result[index]["Count"]) > 1:
        msg = "\n第{}名是「{}」".format(chinese_num[index+1], str(result[index]["content"]))
    return msg


def pihua(data, day):
    group_id = data["group_id"]
    now = datetime.datetime.now()
    today_str = "{}-{}-{}".format(now.year, now.month, now.day)
    today_start_timestamp = int(time.mktime(time.strptime(today_str, '%Y-%m-%d')))

    # today = datetime.date.today()
    # yesterday = today - datetime.timedelta(days=1)
    # yesterday_start_timestamp = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    # yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    # print(yesterday_start_timestamp)
    # print(yesterday_end_time)
    if day == "today":
        result = QQMessage.objects.filter(subject=str(group_id),
                                     timestamp__gte=today_start_timestamp
                                     ).values('content').annotate(Count=Count('content')).order_by('-Count')
        if len(result) > 0 and int(result[0]["Count"] > 1):
            msg = "今天说的最多的批话是「{}」".format(
                str(result[0]["content"])
            )
            for i in range(1, 5):
                msg += parse_msg(result, i)
        else:
            msg = "今天没有人说话呢"

    elif day == "yesterday":
        yesterday_start_timestamp = today_start_timestamp-86400
        result = QQMessage.objects.filter(subject=str(group_id),
                                     timestamp__gte=yesterday_start_timestamp,
                                     timestamp__lt=today_start_timestamp
                                     ).values('content').annotate(Count=Count('content')).order_by('-Count')
        if len(result) > 0 and int(result[0]["Count"] > 1):
            msg = "昨天说的最多的批话是「{}」".format(
                str(result[0]["content"])
            )
            for i in range(1, 5):
                msg += parse_msg(result, i)
        else:
            msg = "昨天没有人说话呢"

    elif day == "month":
        month_start_str = "{}-{}".format(now.year, now.month)
        month_start_timestamp = int(time.mktime(time.strptime(month_start_str, '%Y-%m')))
        result = QQMessage.objects.filter(subject=str(group_id),
                                          timestamp__gte=month_start_timestamp
                                          ).values('content').annotate(Count=Count('content')).order_by('-Count')
        print(result)
        if len(result) > 0 and int(result[0]["Count"] > 1):
            msg = "本月说的最多的批话是「{}」".format(
                str(result[0]["content"])
            )
            for i in range(1, 10):
                msg += parse_msg(result, i)
        else:
            msg = "本月没有人说话呢"

    elif day == "lastmonth":
        if now.month > 1:
            last_month_start_str = "{}-{}".format(now.year, now.month - 1)
            last_month_start_timestamp = int(time.mktime(time.strptime(last_month_start_str, '%Y-%m')))
        else:
            last_month_start_str = "{}-{}".format(now.year - 1, 12)
            last_month_start_timestamp = int(time.mktime(time.strptime(last_month_start_str, '%Y-%m')))
        month_start_str = "{}-{}".format(now.year, now.month)
        month_start_timestamp = int(time.mktime(time.strptime(month_start_str, '%Y-%m')))
        result = QQMessage.objects.filter(subject=str(group_id),
                                          timestamp__gte=last_month_start_timestamp,
                                          timestamp__lt=month_start_timestamp
                                          ).values('content').annotate(Count=Count('content')).order_by('-Count')
        if len(result) > 0 and int(result[0]["Count"] > 1):
            msg = "上个月说的最多的批话是「{}」".format(
                str(result[0]["content"])
            )
            for i in range(1, 10):
                msg += parse_msg(result, i)
        else:
            msg = "上个月没有人说话呢"

    elif day == "week":
        week_start_timestamp = today_start_timestamp - (86400 * now.weekday())
        result = QQMessage.objects.filter(subject=str(group_id),
                                          timestamp__gte=week_start_timestamp
                                          ).values('content').annotate(Count=Count('content')).order_by('-Count')
        if len(result) > 0 and int(result[0]["Count"] > 1):
            msg = "本周说的最多的批话是「{}」".format(
                str(result[0]["content"])
            )
            for i in range(1, 5):
                msg += parse_msg(result, i)
        else:
            msg = "本周没有人说话呢"

    elif day == "lastweek":
        week_start_timestamp = today_start_timestamp - (86400 * now.weekday())
        last_week_start_timestamp = week_start_timestamp - (86400 * 7)
        result = QQMessage.objects.filter(subject=str(group_id),
                                          timestamp__gte=last_week_start_timestamp,
                                          timestamp__lt=week_start_timestamp
                                          ).values('content').annotate(Count=Count('content')).order_by('-Count')
        if len(result) > 0 and int(result[0]["Count"] > 1):
            msg = "上周说的最多的批话是「{}」".format(
                str(result[0]["content"])
            )
            for i in range(1, 10):
                msg += parse_msg(result, i)
        else:
            msg = "上周没有人说话呢"

    send_group_msg(msg, group_id)