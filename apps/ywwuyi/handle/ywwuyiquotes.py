import os
import random
from ywwuyi.cqrequest import send_group_msg
from ywwuyi import cqcode


def ywwuyiQuotes(data):
    for root, dirs, files in os.walk(r"/home/mqmmw/mqmmw/public/static/ywwuyiquotes"):
        img = files[random.randint(0, len(files) - 1)]
        print(img)
        # send_group_msg(cqcode.parse_image("http://mqmmw.qftal.com/static/ywwuyiquotes/" + img), data["group_id"])
        send_group_msg(cqcode.parse_image("http://172.17.0.2/static/ywwuyiquotes/" + img), data["group_id"])