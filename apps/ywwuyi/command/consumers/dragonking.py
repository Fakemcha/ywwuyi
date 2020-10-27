import time,datetime
from ywwuyi.cqrequest import send_group_msg, get_group_member_info
from ywwuyi.models.qq_message import QQMessage
from django.db.models import Count
from ywwuyi.cqcode import parse_at
from ywwuyi.qqproxy.qqinfo import get_group_nick
from ywwuyi.qqproxy.sendmessage import SendQQMessage


def dragonking(qqmessage, day):
    """
    :param qqmessage:
    :param day: yesterday or today
    :return:
    """
    # group_id = data["group_id"]
    group_id = qqmessage.get_group_id()
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_start_timestamp = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    print(today)
    print(yesterday)
    print(yesterday_start_timestamp)
    print(yesterday_end_time)
    if day == "today":
        result = \
        QQMessage.objects.filter(subject=str(group_id), timestamp__gt=yesterday_end_time).values('user_id').annotate(Count=Count('user_id')).order_by('-Count')
        print(result)
        if len(result) > 0:
            name1 = get_group_nick(group_id, qqmessage.get_sender_id())
            # groupMemberInfo = get_group_member_info(group_id, result[0]["user_id"])
            # if groupMemberInfo["data"]["card"]:
            #     name1 = groupMemberInfo["data"]["card"]
            # else:
            #     name1 = groupMemberInfo["data"]["nickname"]
            msg = "今天的龙王是「{}」，已经说了{}条批话了呢".format(
                # parse_at(str(result[0]["user_id"])),
                get_group_nick(group_id, str(result[0]["user_id"])),
                str(result[0]["Count"])
            )
            if len(result) > 1:
                distance = int(result[0]["Count"]) - int(result[1]["Count"])
                # groupMemberInfo = get_group_member_info(group_id, result[1]["user_id"])
                # if groupMemberInfo["data"]["card"]:
                #     name2 = groupMemberInfo["data"]["card"]
                # else:
                #     name2 = groupMemberInfo["data"]["nickname"]
                msg += "\n第二名是「{}」，距离龙王还有{}条，".format(
                    # parse_at(str(result[1]["user_id"])),
                    get_group_nick(group_id, str(result[1]["user_id"])),
                    str(distance)
                )
                if distance >= 5:
                    msg += "要加油呢"
                else:
                    msg += "快要超过了呢"
        else:
            msg = "今天还没有人说话呢"
    elif day == "yesterday":
        result = \
            QQMessage.objects.filter(subject=str(group_id),
                                     timestamp__gte=yesterday_start_timestamp,
                                     timestamp__lte=yesterday_end_time
                                     ).values('user_id').annotate(Count=Count('user_id')).order_by('-Count')
        print(result)
        if len(result) > 0:
            # groupMemberInfo = get_group_member_info(group_id, result[0]["user_id"])
            # if groupMemberInfo["data"]["card"]:
            #     name1 = groupMemberInfo["data"]["card"]
            # else:
            #     name1 = groupMemberInfo["data"]["nickname"]
            msg = "昨天的龙王是「{}」,说了{}条批话呢".format(
                # parse_at(str(result[0]["user_id"])),
                get_group_nick(group_id, str(result[0]["user_id"])),
                str(result[0]["Count"])
            )
            if len(result) > 1:
                # distance = int(result[0]["Count"]) - int(result[1]["Count"])
                # groupMemberInfo = get_group_member_info(group_id, result[1]["user_id"])
                # if groupMemberInfo["data"]["card"]:
                #     name2 = groupMemberInfo["data"]["card"]
                # else:
                #     name2 = groupMemberInfo["data"]["nickname"]
                msg += "\n第二名是「{}」：{}条".format(
                    # parse_at(str(result[1]["user_id"])),
                    get_group_nick(group_id, str(result[1]["user_id"])),
                    str(result[1]["Count"])
                )
            if len(result) > 2:
                # distance = int(result[0]["Count"]) - int(result[1]["Count"])
                # groupMemberInfo = get_group_member_info(group_id, result[2]["user_id"])
                # if groupMemberInfo["data"]["card"]:
                #     name3 = groupMemberInfo["data"]["card"]
                # else:
                #     name3 = groupMemberInfo["data"]["nickname"]
                msg += "\n第三名是「{}」：{}条".format(
                    # parse_at(str(result[1]["user_id"])),
                    get_group_nick(group_id, str(result[2]["user_id"])),
                    str(result[2]["Count"])
                )
        else:
            msg = "昨天没有人说话呢"
    sqm = SendQQMessage()
    sqm.add_group_id(group_id)
    sqm.add_content(msg)
    sqm.send()
    # send_group_msg(msg, group_id)
