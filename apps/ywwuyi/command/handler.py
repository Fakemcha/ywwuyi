from common.logs import write_test_log
# from ywwuyi.config import commandPatterns
from ywwuyi.cqrequest import send_group_msg
from .config import commandPatterns
import threading
import json
from .pattern import CommandPattern


class CommandHandler(object):
    """使用单例模式"""

    def __init__(self, commandPatterns):
        # 初始化 命令路由，生成一个list [ CommandPattern, CommandPattern, CommandPattern ]
        self.commandPatterns = commandPatterns

    def handle(self, qqmessage):
        for cp in self.commandPatterns:
            is_match, is_end = cp.match(qqmessage)
            if is_match:
                # send_group_msg("噔噔噔噔，收到信号了呢", data["group_id"])
                method = cp.get_method()
                kwargs = cp.get_kwargs()
                # if kwargs:
                #     t = threading.Thread(target=method, args=(data,), kwargs=kwargs)
                # else:
                #     t = threading.Thread(target=method, args=(data,))
                t = threading.Thread(target=method, args=(qqmessage,), kwargs=kwargs)
                t.start()
            if is_end:
                break

    def get_command_patterns(self):
        return self.commandPatterns

    def get_command_patterns_name(self):
        commandPatternsNames = []
        for cp in self.commandPatterns:
            commandPatternsNames.append(cp.description)
        return commandPatternsNames

    def add_command_pattern(self, cp):
        self.commandPatterns.append(cp)

        # commandPatternsNames = {}
        # for i in range(len(self.commandPatterns)):
        #     commandPatternsNames[str(i)] = self.commandPatterns[i].description
        # return commandPatternsNames

    def delete_command_pattern(self, description):
        for i in range(len(self.commandPatterns)):
            cp = self.commandPatterns[i]
            if cp.description == description:
                del self.commandPatterns[i]
                return True
        return False


commandHandler = CommandHandler(commandPatterns)