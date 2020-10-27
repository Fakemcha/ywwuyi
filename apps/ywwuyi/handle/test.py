from common.logs import write_test_log
from ywwuyi.cqrequest import send_group_msg
from ywwuyi.cqcode import parse_at
import os
import time
import random
from ywwuyi import cqcode

def test(data):
    # write_test_log("你好", filename="test.log")
    # send_group_msg(data, data["group_id"])
    # send_group_msg(r"[CQ:image,file=http://mqmmw.qftal.com:1551/static/cqcache/ywwuyi.jpg]", data["group_id"])
    # send_group_msg(parse_at("qqhao"), data["group_id"])
    send_group_msg("噔噔噔噔，收到信号了呢", data["group_id"])
    # for root, dirs, files in os.walk(r"/home/mqmmw/mqmmw/public/static/cqcache"):
    #     send_group_msg(files, data["group_id"])


def timetest():
    send_group_msg("{} 定时测试 线程1".format(time.asctime(time.localtime(time.time()))), 532799508)

def timetest2():
    send_group_msg("{} 定时测试 线程2".format(time.asctime(time.localtime(time.time()))), 532799508)

def timetest3():
    send_group_msg("{} 定时测试 线程3".format(time.asctime(time.localtime(time.time()))), 532799508)

def timetest4():
    send_group_msg("{} 定时测试 线程4".format(time.asctime(time.localtime(time.time()))), 532799508)

def timetest5():
    send_group_msg("{} 定时测试 线程5".format(time.asctime(time.localtime(time.time()))), 532799508)

def ywwuyiQuotesTest():
    pass
    # for root, dirs, files in os.walk(r"/home/mqmmw/mqmmw/public/static/ywwuyiquotes"):
    #     img = files[random.randint(0, len(files) - 1)]
    #     # print(img)
    #     write_test_log(time.asctime(time.localtime(time.time())))
    #     send_group_msg(cqcode.parse_image("http://mqmmw.qftal.com/static/ywwuyiquotes/" + img), 532799508)