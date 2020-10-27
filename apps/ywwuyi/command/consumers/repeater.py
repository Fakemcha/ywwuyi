# -*- coding: UTF-8 -*-
# from ywwuyi.cqrequest import send_group_msg
from ywwuyi.qqproxy.sendmessage import SendQQMessage
from ywwuyi.command.consumers.cgc import cgm

class Repeater(object):

    def __init__(self, repeat_check_count=2):
        self.repeat_check_count = repeat_check_count
        self.has_repeat = {}
        self.pre_message = {}

    def repeat(self, group_id, message):
        if str(group_id) in self.pre_message:
            if len(self.pre_message[str(group_id)]) < self.repeat_check_count:
                return False
            for pre_msg in self.pre_message[str(group_id)]:
                if pre_msg != message:
                    self.has_repeat[str(group_id)] = False
                    return False
            if not str(group_id) in self.has_repeat or not self.has_repeat[str(group_id)]:
                self.has_repeat[str(group_id)] = True
                return True
        else:
            return False

    def save_message(self, group_id, message):
        if str(group_id) in self.pre_message:
            l = self.pre_message[str(group_id)]
            l.append(message)
            if len(l) > self.repeat_check_count:
                l.pop(0)
            self.pre_message[str(group_id)] = l
        else:
            self.pre_message[str(group_id)] = [message]


rpt = Repeater()


def repeat(qqmessage):
    group_id = qqmessage.get_group_id()
    message = qqmessage.get_content()
    rpt.save_message(group_id, message)
    if rpt.repeat(group_id, message):
        sqm = SendQQMessage()
        sqm.add_group_id(group_id)
        sqm.add_content(message)
        sqm.send()
    if cgm.check(message):
        sqm = SendQQMessage()
        sqm.add_group_id(group_id)
        sqm.add_content("猜对了,mua!")
        sqm.send()









