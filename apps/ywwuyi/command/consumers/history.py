import datetime
import time
import string
import json
from common.request import request_by_url
from urllib.parse import quote
from ywwuyi.qqproxy.sendmessage import SendQQMessage


def history(qqmessage):
    time_now = datetime.datetime.now().timetuple()
    date = "{}%2F{}".format(time_now.tm_mon, time_now.tm_mday)
    url = "http://v.juhe.cn/todayOnhistory/queryEvent.php?date={}&key=74d876c3637aa01cfa55722e68f20153".format(date)
    quote_url = quote(url, safe=string.printable)
    request_res = request_by_url(quote_url)
    request_dict = json.loads(request_res)
    sqm = SendQQMessage()
    sqm.add_group_id(qqmessage.get_group_id())
    for i in request_dict["result"]:
        history_date = i["date"]
        history_title = i["title"]
        sqm.add_content("{}\n{}\n".format(history_date, history_title))
    sqm.send()


# def history():
#     time = datetime.datetime.now().timetuple()
#     date = "{}%2F{}".format(time.tm_mon, time.tm_mday)
#     url = "http://v.juhe.cn/todayOnhistory/queryEvent.php?date={}&key=74d876c3637aa01cfa55722e68f20153".format(date)
#     quote_url = quote(url, safe=string.printable)
#     request_res = request_by_url(quote_url)
#     request_dict = json.loads(request_res)
#     msg = ""
#     qq_msg_max_length = 600
#     for i in request_dict["result"]:
#         history_date = i["date"]
#         history_title = i["title"]
#         msg += "{}\n{}\n".format(history_date, history_title)
#         if len(msg) > qq_msg_max_length:
#             print(msg)
#             sqm = SendQQMessage()
#             sqm.add_group_id()
#             # send_group_msg(msg, group_id)
#             msg = ""
#     print(msg)

    # send_group_msg(msg, group_id)
