# -*- coding: UTF-8 -*-
import json
import time
from ywwuyi.config import mirai_interface_url
from common.request import post_by_url


max_message_length = 600

class SendQQMessage(object):

    def __init__(self):
        self.message_chain = []
        self.private_id = []
        self.group_id = []

    def add_content(self, text, type="Plain"):
        d = {
            "type": type,
            "text": text
        }
        self.message_chain.append(d)

    def add_image(self, url):
        d = {
            "type": "Image",
            "url": url
        }
        self.message_chain.append(d)

    def add_private_id(self, private_id):
        self.private_id.append(private_id)

    def add_group_id(self, group_id):
        self.group_id.append(group_id)

    def __send_group_message(self, group_id):
        from ywwuyi.qqproxy.mirai import mirai_session
        message_length = 0
        last_send_index = 0
        index = 0
        # for message_cabin in self.message_chain:
        for i in range(len(self.message_chain)):

            message_cabin = self.message_chain[i]
            if message_cabin["type"] == "Plain":
                message_length += len(message_cabin["text"])

            if message_length > max_message_length:
                d = {
                    "sessionKey": mirai_session.get_session_key(),
                    # "messageChain": [{ "type": "Plain","text": str(index) + "\n" }] + self.message_chain[last_send_index:i],
                    "messageChain": self.message_chain[last_send_index:i],
                    "target": int(group_id)
                }
                post_by_url(mirai_interface_url + "sendGroupMessage", json.dumps(d))
                last_send_index = i
                message_length = 0
                index += 1
                time.sleep(1)
        d = {
            "sessionKey": mirai_session.get_session_key(),
            # "messageChain": [{ "type": "Plain","text": str(index) + "\n" }] + self.message_chain[last_send_index:],
            "messageChain": self.message_chain[last_send_index:],
            "target": int(group_id)
        }
        ret = post_by_url(mirai_interface_url + "sendGroupMessage", json.dumps(d))
        print(ret)
        print(ret.text)
        print(ret.content)

    def send(self):
        for private_id in self.private_id:
            pass

        for group_id in self.group_id:
            # print("---------send----------")
            self.__send_group_message(group_id)