from common.logs import write_test_log
from ywwuyi.cqrequest import send_group_msg
from ywwuyi.cqcode import parse_at
import os
import time
import random
from ywwuyi import cqcode
from ywwuyi.models.qq_message import QQMessage
import re
import subprocess


def test(data):
    # write_test_log("你好", filename="test.log")
    # send_group_msg(data, data["group_id"])
    # send_group_msg(r"[CQ:image,file=http://mqmmw.qftal.com:1551/static/cqcache/ywwuyi.jpg]", data["group_id"])
    # send_group_msg(parse_at("qqhao"), data["group_id"])
    # send_group_msg("噔噔噔噔，收到信号了呢", data["group_id"])
    # for root, dirs, files in os.walk(r"/home/mqmmw/mqmmw/public/static/cqcache"):
    #     send_group_msg(files, data["group_id"])
    result = QQMessage.objects.filter(subject="92172618")
    print("长度")
    print(len(result))
    index = 0
    pre_contnet = ""
    pre_user_id = ""
    content = ""
    user_id = ""
    os.unlink(r"/home/seq2seq-master/data/question.txt")
    os.unlink(r"/home/seq2seq-master/data/answer.txt")
    for i in result:
        if "[CQ" in i.content:
            continue
        if "^M" in i.content:
            continue
        if "d" in i.content:
            continue
        i.content = re.sub(r'[\x00-\x1f]', '', i.content)

        pre_user_id = user_id
        user_id = i.user_id
        if pre_user_id == i.user_id:
            content += " " + i.content.replace("\r", "").replace("\n", "").replace(" ", "")
        else:
            if pre_user_id == "463705592":
                index += 1
                if index == 4:
                    break
                print("-" * 50)
                print("Q:" + pre_contnet)
                print("A:" + content)
                print("-" * 50)
                # with open("/home/seq2seq-master/data/question.txt", "a+") as f:
                #     f.write(pre_contnet.replace("\r", "").replace("\n", "").replace(" ", "") + "\n")
                # with open("/home/seq2seq-master/data/answer.txt", "a+") as f:
                #     f.write(content.replace("\r", "").replace("\n", "").replace(" ", "") + "\n")
                # subprocess.Popen("echo '{}' >> /home/seq2seq-master/data/question.txt".format(
                #     pre_contnet.replace("\r", "").replace("\n", "").replace(" ", "")
                # ),
                # shell=True)
                # subprocess.Popen("echo '{}' >> /home/seq2seq-master/data/answer.txt".format(
                #     content.replace("\r", "").replace("\n", "").replace(" ", "")
                # ))
                os.system(
                    "echo '{}' >> /home/seq2seq-master/data/question.txt".format(
                        pre_contnet.replace("\r", "").replace("\n", "").replace(" ", "")
                    )
                )
                os.system(
                    "echo '{}' >> /home/seq2seq-master/data/answer.txt".format(
                        content.replace("\r", "").replace("\n", "").replace(" ", "")
                    )
                )
            pre_contnet = content
            content = i.content

        # pre_contnet = content
        # pre_user_id = user_id
        # content = i.content
        # user_id = i.user_id
        # if pre_user_id != user_id and user_id == "463705592":
        #     print("-"*50)
        #     print("Q:" + pre_contnet)
        #     print("A:" + content)
        #     print("-" * 50)
        # index += 1
        # if index == 100:
        #     break
        # print(i.content)
    send_group_msg("噔噔噔噔，收到信号了呢", data["group_id"])


def send_task_name(data):
    #
    # from ywwuyi.timedtask.controller import timedtaskController
    # msg = timedtaskController.get_task_name()
    # msg = "test"
    from ywwuyi.timedtask.controller import timedtaskController
    msg = timedtaskController.get_task_name()
    print("task:")
    print(msg)
    print(timedtaskController.get_tasks())
    if msg == "":
        msg = "没有任务"
    send_group_msg(msg, 532799508)


def qidong(data):
    from ywwuyi.timedtask.controller import timedtaskController
    timedtaskController.run()
    msg = "任务启动成功:\n"
    msg += timedtaskController.get_task_name()
    send_group_msg(msg, 532799508)

def del_task(data):
    message = data["message"]
    name = message.split(" ")[1]
    from ywwuyi.timedtask.controller import timedtaskController
    print(name)
    timedtaskController.cancel_task(name)
