# -*- coding: UTF-8 -*-
import json
import websocket
from common.request import post_by_url
from ywwuyi.config import robot_id, mirai_interface_url, mirai_auth_key
from ywwuyi.qqproxy.qqmessage import MiraiMessage
from ywwuyi.command.handler import commandHandler
from ywwuyi.models.qq_message import QQMessage


def on_message(ws, message):
    # print("message")
    # print(ws)
    print("=" * 60)
    print(message)
    with open("/home/message.json", mode="a+") as f:
        f.write(str(message) + "\n")
    mm = MiraiMessage(message)
    qm = QQMessage(
        subject=str(mm.get_group_id()),
        user_id=str(mm.get_sender_id()),
        content=str(mm.get_content()),
        type="group",
        timestamp=mm.get_message_time()
    )
    qm.save()
    commandHandler.handle(mm)
    print("=" * 60)


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")


class MiraiSession(object):

    def __init__(self):
        self.session_key = None

    # listen_mirai
    def start(self):
        # 获取session
        data = {"authKey": mirai_auth_key}
        auth_url = mirai_interface_url + "auth"
        r = post_by_url(auth_url, data=json.dumps(data))
        self.session_key = json.loads(r.text)["session"]
        # mirai_session_key = session_key

        # 激活session
        data = {"sessionKey": self.session_key, "qq": robot_id}
        verify_url = mirai_interface_url + "verify"
        r = post_by_url(verify_url, data=json.dumps(data))
        if json.loads(r.text)["msg"] == "success":
            url = r"ws://ywwuyi.cc:1571/all?sessionKey={}".format(self.session_key)
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
            ws.run_forever()

    def get_session_key(self):
        return self.session_key


# mirai_session = MiraiSession()