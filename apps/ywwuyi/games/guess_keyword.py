# -*- coding: UTF-8 -*-
import os
import random
import json
import copy
from ywwuyi.cqrequest import send_private_msg, send_group_msg, get_group_member_info, get_group_info, ban
from settings import PROJECT_DIR
from ywwuyi.config import robot_id


class ForbiddenWordsGame(object):

    def __init__(self):
        self.forbidden_ont_word_list = [
            "爬",
            "稳",
            "疯",
            "慌",
            "打",
            "上",
            "下",
            "学",
            "来",
            "给",
            "波",
            "恰",
            "飞",
            "抽",
            "对",
            "亏",
            "惨",
            "好",
            "快",
            "死",
            "笑",
            "大",
            "小",
            "去",
            "奶",
            "留",
            "菜",
            "星",
            "动",
            "车",
            "过",
            "肉",
            "氪",
            "钱",
            "草",
            "送",
            "猛",
            "强",
            "辣",
            "买",
            "爽",
            "猫",
            "觉",
            "吊",
            "梗",
            "硬",
            "软",
            "天",
            "看",
            "男",
            "女",
            "搞",
            "土",
            "图",
            "鱼",
            "冷",
            "热",
            "刷",
        ]

        self.forbidden_two_word_list = [
            "可以",
            "不行",
            "不能",
            "不好",
            "不是",
            "不会",
            "不要",
            "不懂",
            "知道",
            "一般",
            "没有",
            "辣鸡",
            "牛批",
            "菊花",
            "金牌",
            "禁止",
            # "塑料",
            # "黑铁",
            # "白银",
            "黄金",
            # "白金",
            # "钻石",
            # "王者",
            "爽哥",
            "龙王",
            "不准",
            "建议",
            "测试",
            "活动",
            "胖子",
            "还行",
            "什么",
            "怎么",
            "锤子",
            "还有",
            "真实",
            "离谱",
            # "妈妈",
            "道理",
            "黄色",
            "公主",
            "属性",
            "苹果",
            "游戏",
            "爆炸",
            "经典",
            "确实",
            "更新",
            "机会",
            "技能",
            "上当",
            "批话",
            "服务",
            "老师",
            "学生",
            "钓鱼",
            "禁言",
            "暴力",
            "翻译",
            "干嘛",
        ]

        self.player_dict = None
        self.init_player_dict()

    def init_player_dict(self):
        self.player_dict = {
            "92172618": {
                "463705592": None,
                "602404187": None,
                "742046286": None,
                "768303015": None,
                "844266359": None,
                "864603443": None,
                "903059704": None,
                "1227869031": None,
                "1787317901": None,
            }
        }
        d = {"keyword": [], "nickname": None, "powder": 0}
        for group_id in self.player_dict:
            for user_id in self.player_dict[group_id]:
                self.player_dict[group_id][user_id] = copy.deepcopy(d)
        print(self.player_dict)

    def read_forbidden_words(self):
        if os.path.exists(PROJECT_DIR + "/tmp/keywords.json"):
            print("读取禁语")
            with open(PROJECT_DIR + "/tmp/keywords.json", mode="r") as f:
                d = json.loads(f.read())
            self.player_dict = d.copy()
            print(d)
        return

    def save_forbidden_words(self):
        with open(PROJECT_DIR + "/tmp/keywords.json", mode="w") as f:
            f.write(json.dumps(self.player_dict, ensure_ascii=False))

    def explode(self, group_id, user_id, time=60):
        msg = "「{}」爆炸了".format(self.player_dict[group_id][user_id]["nickname"])
        send_group_msg(msg, group_id)
        ban(group_id, user_id, time)

    def make_forbidden_words(self, data):
        self.init_player_dict()
        # 生成禁语
        forbidden_one_word_len = len(self.forbidden_ont_word_list)
        forbidden_two_word_len = len(self.forbidden_two_word_list)

        for play_group_id in self.player_dict:
            players = self.player_dict[play_group_id]
            for player_id in players:
                print(play_group_id)
                print(player_id)
                _keyword = self.forbidden_ont_word_list[random.randint(0, forbidden_one_word_len - 1)]
                self.player_dict[play_group_id][player_id]["keyword"].append(_keyword)
                rand_num1 = random.randint(0, forbidden_two_word_len - 1)
                _keyword = self.forbidden_two_word_list[rand_num1]
                self.player_dict[play_group_id][player_id]["keyword"].append(_keyword)
                while True:
                    rand_num2 = random.randint(0, forbidden_two_word_len - 1)
                    if rand_num2 != rand_num1:
                        break
                _keyword = self.forbidden_two_word_list[rand_num2]
                self.player_dict[play_group_id][player_id]["keyword"].append(_keyword)

        print("x" * 50)
        print(self.player_dict)
        print("x" * 50)

        # 发送禁语
        for play_group_id in self.player_dict:
            groupInfo = get_group_info(play_group_id)
            group_name = groupInfo["data"]["group_name"]

            players = self.player_dict[play_group_id]

            for send_player_id in players:
                msg = "小游戏，勾引群友说出对应的禁语，群友就会爆炸[v2.33]\n禁语「{}」:\n".format(group_name)
                for forbidden_player_id in players:
                    if forbidden_player_id != send_player_id:
                        if self.player_dict[play_group_id][forbidden_player_id]["nickname"] is None:
                            groupMemberInfo = get_group_member_info(play_group_id, forbidden_player_id)
                            if groupMemberInfo["data"]["card"]:
                                forbidden_player_name = groupMemberInfo["data"]["card"]
                            else:
                                forbidden_player_name = groupMemberInfo["data"]["nickname"]
                            self.player_dict[play_group_id][forbidden_player_id]["nickname"] = forbidden_player_name
                        else:
                            forbidden_player_name = self.player_dict[play_group_id][forbidden_player_id]["nickname"]
                        msg += "「{}」:「{}」「{}」「{}」\n".format(
                            forbidden_player_name,
                            self.player_dict[play_group_id][forbidden_player_id]["keyword"][0],
                            self.player_dict[play_group_id][forbidden_player_id]["keyword"][1],
                            self.player_dict[play_group_id][forbidden_player_id]["keyword"][2]
                        )
                send_private_msg(msg, send_player_id)

        # 保存禁语
        self.save_forbidden_words()

        return

    def check_keyword(self, data):
        # print(player_dict)
        if "group_id" not in data:
            return
        group_id = str(data["group_id"])
        user_id = str(data["user_id"])
        message = str(data["message"])
        if group_id not in self.player_dict or user_id not in self.player_dict[group_id]:
            return

        keyword_list = self.player_dict[group_id][user_id]["keyword"]
        if keyword_list:
            ban_time = 0
            for keyword in keyword_list:
                # print(keyword)
                if keyword in message:
                    ban_time += 60
            if ban_time > 0:
                self.explode(group_id, user_id, ban_time)
                self.make_forbidden_words(None)

    def my_forbidden_word(self, data):
        group_id = str(data["group_id"])
        user_id = str(data["user_id"])
        message = str(data["message"])
        message_list = message.split(" ")
        if len(message_list) != 2:
            send_group_msg("指令格式错误", group_id)
            return
        else:
            guess_word = message_list[1]
        if guess_word in self.player_dict[group_id][user_id]["keyword"]:
            send_group_msg("呐呐呐，你想让谁爆炸？", group_id)
            self.player_dict[group_id][user_id]["powder"] += 1
            self.save_forbidden_words()
        else:
            send_group_msg("多捞啊", group_id)
            self.explode(group_id, user_id, 30)

    def check_powder(self, data):
        print("检查爆炸")
        group_id = str(data["group_id"])
        user_id = str(data["user_id"])
        message = str(data["message"])
        powder = self.player_dict[group_id][user_id]["powder"]
        print(powder)

        if powder > 0:
            explode_user_id = message.replace("[CQ:at,qq=", "").replace("]", "").replace(" ", "")
            print(explode_user_id)
            if explode_user_id == str(robot_id):
                send_group_msg("想造反？", group_id)
                self.explode(group_id, user_id)
            else:
                self.explode(group_id, explode_user_id)
            self.player_dict[group_id][user_id]["powder"] -= 1
            self.save_forbidden_words()



forbidden_words_game = ForbiddenWordsGame()


if __name__ == '__main__':
    pass