import re


def transferMeaning(s):
    return str(s).replace(":", "\:")#.replace("[", "\[").replace("]", "\]")


class CommandPattern(object):

    def __init__(self, regex, method, description="", private=None, group=None, kwargs=None, isEnd=True):
        """
        :param regex: 命令正则表达式
        :param method: 处理函数
        :param isEnd: 是否结束，if False，会继续寻找其他相匹配的命令模型
        """

        self.regex = regex
        self.method = method
        self.isEnd = isEnd
        self.private = private
        self.group = group
        self.kwargs  = kwargs
        if private is None and group is None:
            self.private = ["*"]
            self.group = ["*"]
        if description == "":
            self.description = regex
        else:
            self.description = description

    def match(self, qqmessage):
        """
        :param qqmessage:
        :return: 是否匹配，是否结束
        """
        content = qqmessage.get_content()
        message_type = qqmessage.get_message_type()
        message_type_match_flag = False
        if message_type == qqmessage.privateMessage:
            if self.private:
                if "*" in self.private:
                    message_type_match_flag = True
                elif int(qqmessage.get_sender_id()) in self.private or str(qqmessage.get_sender_id()) in self.private:
                    message_type_match_flag = True
        elif message_type == qqmessage.groupMessage:
            if self.group:
                if "*" in self.group:
                    message_type_match_flag = True
                elif int(qqmessage.get_group_id()) in self.group or str(qqmessage.get_group_id()) in self.group:
                    message_type_match_flag = True

        if message_type_match_flag:
            is_match = bool(re.search(transferMeaning(self.regex), content))
            if is_match:
                print("匹配到command:" + content)
                return is_match, self.isEnd
            else:
                return False, False
        else:
            # 没匹配到，不能结束
            return False, False

        # message = data["message"]
        # message_type = data["message_type"]
        # message_type_match_flag = False
        # if message_type == "private":
        #     if self.private:
        #         if "*" in self.private:
        #             message_type_match_flag = True
        #         elif data["user_id"] in self.private:
        #                 message_type_match_flag = True
        # elif message_type == "group":
        #     if self.group:
        #         if "*" in self.group:
        #             message_type_match_flag = True
        #         elif data["group_id"] in self.group:
        #                 message_type_match_flag = True
        # if message_type_match_flag:
        #     is_match = bool(re.search(transferMeaning(self.regex), message))
        #     if is_match:
        #         print("匹配到command:" + message)
        #         return is_match, self.isEnd
        #
        # return False, False

    def get_method(self):
        return self.method

    def get_kwargs(self):
        if self.kwargs:
            return self.kwargs
        else:
            return {}
        # return self.kwargs
