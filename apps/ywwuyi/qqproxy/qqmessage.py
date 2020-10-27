# -*- coding: UTF-8 -*-
import abc
import json


class QQMessage(metaclass=abc.ABCMeta):

    privateMessage = 1
    groupMessage = 2

    @abc.abstractmethod
    def get_message_type(self):
        # 消息类型，Group/Private
        pass

    @abc.abstractmethod
    def get_content(self):
        # 消息内容
        pass

    @abc.abstractmethod
    def get_sender_id(self):
        # 消息发送者id
        pass

    @abc.abstractmethod
    def get_group_id(self):
        # 消息来源群id
        pass

    @abc.abstractmethod
    def get_message_time(self):
        # 消息发送时间
        pass

    # @abc.abstractmethod
    def is_private_message(self):
        return self.message_type == QQMessage.privateMessage

    # @abc.abstractmethod
    def is_group_message(self):
        return self.message_type == QQMessage.groupMessage


class MiraiMessage(QQMessage):

    def __init__(self, message):
        self.content = ""
        self.message_type = None
        self.message_id = None
        self.message_time = None
        self.group_id = None
        self.group_nick = None
        message_json = json.loads(message)
        if message_json["type"] == "GroupMessage":
            self.message_type = 2
            for message_cabin in message_json["messageChain"]:
                if message_cabin["type"] == "Source":
                    self.message_id = message_cabin["id"]
                    self.message_time = message_cabin["time"]
                elif message_cabin["type"] == "Plain":
                    self.content += message_cabin["text"]
            self.sender_id = message_json["sender"]["id"]
            self.sender_nick = message_json["sender"]["memberName"]
            self.group_id = message_json["sender"]["group"]["id"]
            self.group_nick = message_json["sender"]["group"]["name"]

    def get_message_type(self):
        return self.message_type

    def get_content(self):
        return self.content

    def get_sender_id(self):
        return self.sender_id

    def get_sender_nick(self):
        return self.sender_nick

    def get_group_id(self):
        return self.group_id

    def get_message_time(self):
        return self.message_time
