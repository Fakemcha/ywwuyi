# -*- coding: UTF-8 -*-
import json
import random
from ywwuyi.qqproxy.sendmessage import SendQQMessage
from ywwuyi.models.lyric import Lyric

class CGM(object):
    def __init__(self):
        self.guessed = False
        self.lyric = None

    def guess(self):
        self.guessed = False
        # self.ran = random.randint(0, len(self.l))
        lyric = Lyric.objects.order_by('?')[0]
        self.lyric = lyric
        l = str(lyric.lyric).split('\n')
        ret = ''
        ran = random.randint(10, len(l) - 10)
        for i in range(ran, ran + 4):
            ret += (l[i] + '\n')
        return ret

    def check(self, word):
        if self.lyric:
            if not self.guessed and self.lyric.title == word:
                self.guessed = True
                return True
            else:
                return False
    def gemin(self):
        if self.lyric:
            return self.lyric.title
        else:
            return '还没有猜'

cgm = CGM()

def caigemin(qqmessage):
    group_id = qqmessage.get_group_id()
    guess_lyric = cgm.guess()
    sqm = SendQQMessage()
    sqm.add_group_id(group_id)
    sqm.add_content(guess_lyric)
    sqm.send()

def gemin(qqmessage):
    group_id = qqmessage.get_group_id()
    gemin = cgm.gemin()
    sqm = SendQQMessage()
    sqm.add_group_id(group_id)
    sqm.add_content(gemin)
    sqm.send()


# class CGC(object):
#     def __init__(self):
#         singer_knows = [
#             "许嵩",
#             "周杰伦",
#             # "陈奕迅",
#             # "杨丞琳",
#             # "潘玮柏",
#             "林俊杰",
#             # "李玖哲",
#             # "薛之谦",
#             # "蔡依林",
#             # "凤凰传奇"
#         ]
#         path = "/home/music.json"
#         self.l = []
#         self.geshou = []
#         file = open(path, 'r', encoding='utf-8')
#         for line in file.readlines():
#             s = json.loads(line)
#             if s["singer"] in singer_knows:
#                 self.l.append(s)
#                 self.geshou.append(s["singer"])
#         self.ran = 0
#         self.guessed = False
#         # print("==" *50)
#         # print(set(self.geshou))
#         # print("==" * 50)

#     def guess(self):
#         self.guessed = False
#         self.ran = random.randint(0, len(self.l))
#         print(self.l[self.ran])
#         return self.l[self.ran]["geci"]

#     def check(self, word):
#         # print(self.l[self.ran])
#         if not self.guessed and self.l[self.ran]["song"] == word:
#             self.guessed = True
#             return True
#         else:
#             return False


# cgc = CGC()


# def caigeci(qqmessage):
#     group_id = qqmessage.get_group_id()
#     geci = cgc.guess()
#     sqm = SendQQMessage()
#     sqm.add_group_id(group_id)
#     if len(geci) > 12:
#         ran = random.randint(10, len(geci) - 10)
#     else:
#         ran = random.randint(4, len(geci) - 4)
#     for i in geci[ran:ran + 2]:
#         sqm.add_content(str(i) + "\n")
#     sqm.send()