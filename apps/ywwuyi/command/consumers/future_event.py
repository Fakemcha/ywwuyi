# -*- coding: UTF-8 -*-
import time
import datetime
from ywwuyi.cqrequest import send_group_msg
from ywwuyi.qqproxy.sendmessage import SendQQMessage


fes = [
    {
        "date": "2018-10-20",
        "name": "皇倒祭日"
    },
    {
        "date": "2018-11-03",
        "name": "IG赢得S8冠军"
    },
    {
        "date": "2019-11-10",
        "name": "FPX赢得S9冠军"
    },
    {
        "date": "2020-08-17",
        "name": "长者生日"
    },
    {
        "date": "2020-09-01",
        "name": "小欧归来",
        "group": ["532799508", "92172618"]
    },
    {
        "date": "2020-09-05",
        "name": "妙妙屋团建🤺",
        "group": ["532799508", "92172618"]
    },
    {
        "date": "2020-09-23",
        "name": "秋分",
    },
    {
        "date": "2020-09-25",
        "name": "S10赛事开始",
    },
    {
        "date": "2020-10-01",
        "name": "中秋节 / 国庆节"
    },
    {
        "date": "2020-10-08",
        "name": "S10小组赛 SN/G2出线 MCX/TL淘汰",
    },
    {
        "date": "2020-10-09",
        "name": "S10小组赛 DWG/JDG出线 PSG/RGE淘汰",
    },
    {
        "date": "2020-10-10",
        "name": "S10小组赛 GEN/FNC出线 LGD/TSM淘汰",
    },
    {
        "date": "2020-10-11",
        "name": "S10小组赛 TES/DRX出线 FLY/UOL淘汰",
    },
    {
        "date": "2020-10-12",
        "name": "许嵩发布单曲《放肆》",
        "group": [""]
    },
    {
        "date": "2020-10-15",
        "name": "S10淘汰赛 DWG 3:0 DRX",
    },
    {
        "date": "2020-10-16",
        "name": "S10淘汰赛 SN 3:1 JDG",
    },
    {
        "date": "2020-10-17",
        "name": "S10淘汰赛 TES 3:2 FNC,创造了S赛中的第一次让二追三",
    },
    {
        "date": "2020-10-17",
        "name": "沈逸专场演讲《美国大选：见证霸权的黄昏》",
        "group": ["532799508", "92172618"]
    },
    {
        "date": "2020-10-18",
        "name": "S10淘汰赛 GEN 0:3 G2",
    },
    {
        "date": "2020-10-24",
        "name": "S10半决赛 DWG 3:1 G2",
    },
    {
        "date": "2020-10-25",
        "name": "S10半决赛 SN 3:1 TES",
    },
    {
        "date": "2020-10-31",
        "name": "S10总决赛 SN vs DWG",
    },
    {
        "date": "2020-11-02",
        "name": "胖子生日",
        "group": ["532799508", "92172618"]
    },
    {
        "date": "2020-11-03",
        "name": "美国大选",
    },
    {
        "date": "2020-11-19",
        "name": "《赛博朋克2077》发售"
    },
    {
        "date": "2021-01-08",
        "name": "《白箱》发售",
        "group": ["532799508", "92172618"]
    },
]


class FutureEvent(object):
    def __init__(self):
        self.events = []
        for d in fes:
            self.registe(d)

    def registe(self, d):
        self.events.append(d)

    def check(self, qqmessage):
        if qqmessage.is_group_message():
            msg = ""
            group_id = str(qqmessage.get_group_id())
            for fe in self.events:
                if not "group" in fe or group_id in fe["group"]:
                    date = datetime.datetime.strptime(fe["date"], "%Y-%m-%d")
                    today = time.strftime("%Y-%m-%d", time.localtime())
                    # today = time.localtime()
                    today = datetime.datetime.strptime(today, "%Y-%m-%d")
                    if date > today:
                        distance = (date - today).days
                        msg += "距离 {} 还有 {} 天\n".format(fe["name"], distance)
                    elif date == today:
                        msg += "今天 {}\n".format(fe["name"])
            sqm = SendQQMessage()
            sqm.add_group_id(qqmessage.get_group_id())
            sqm.add_content(msg)
            sqm.send()
        # send_group_msg(msg, data["group_id"])
        # if qqmessage.is_group_message():
        #     sqm = SendQQMessage()
        #     sqm.add_group_id(qqmessage.get_group_id())
        #     sqm.add_content(msg)
        #     sqm.send()


future_event = FutureEvent()

if __name__ == '__main__':
    pass