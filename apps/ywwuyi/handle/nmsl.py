import json
import random
from ywwuyi import config
from collections import OrderedDict
from pypinyin import lazy_pinyin
from ywwuyi.cqrequest import send_group_msg


def nmslTransilate(data):
    message = data["message"]
    content = ''
    message_split = message.split(' ')
    for i in range(len(message_split) - 1):
        content += message_split[i + 1]

    res_handleword = ""
    SWITCH_DICT = {}

    if "部长" in content:
        content = content.replace("部长", "鸡哥")

    # 把原本的+替换为%+%
    content = content.replace("+", r"%+%")

    # 读取json文件
    WORD_MAP_FILE_PATH = str(config.cq_cache_path) + r"/NMSL_WORD_MAP.json"
    with open(WORD_MAP_FILE_PATH, 'r', encoding="utf-8") as f:
        WORD_MAP_JSON = f.read()
    WORD_MAP = json.loads(WORD_MAP_JSON, object_pairs_hook=OrderedDict)

    # 翻译词语
    for key in WORD_MAP:
        # 遍历关键字
        while (1):
            key_in_content = content.find(key)
            # 没有关键字则返回
            if key_in_content == -1:
                break
            # 有关键字，将关键字替换为@，如果关键字长度大于1，则在后面加+
            else:
                str_replace = "@" + "+" * (len(key) - 1)
                content = content.replace(key, str_replace, 1)
                # print(type(WORD_MAP[key]))
                if type(WORD_MAP[key]) == list:
                    random_index = random.randint(1, len(WORD_MAP[key])) - 1
                    SWITCH_DICT[str(key_in_content)] = WORD_MAP[key][random_index]
                else:
                    SWITCH_DICT[str(key_in_content)] = WORD_MAP[key]

    # print(SWITCH_DICT)
    # print(content)
    # print(SWITCH_DICT)

    # 把@符号换回emoji
    is_pre_at = False
    for i in range(len(content)):
        if content[i] == "@":
            is_pre_at = True
        else:
            if is_pre_at and content[i] == "+":
                continue
            else:
                is_pre_at = False
        if str(i) in SWITCH_DICT:
            res_handleword = res_handleword + SWITCH_DICT[str(i)]
        else:
            res_handleword = res_handleword + content[i]

    # print(content)
    # print(res_handleword)
    res = ""

    # 读取json文件
    PY_MAP_FILE_PATH = str(config.cq_cache_path) + r"/NMSL_PY_MAP.json"
    with open(PY_MAP_FILE_PATH, 'r', encoding="utf-8") as f:
        PY_MAP_JSON = f.read()
    # print(PY_MAP_JSON)
    PY_MAP = json.loads(PY_MAP_JSON, object_pairs_hook=OrderedDict)

    # 翻译拼音
    emoji_count = 0
    is_emoji = False
    is_emojiend = False
    res_list = []
    has_append = False
    for tr in res_handleword:
        if emoji_count % 30 == 0:
            if emoji_count != 0 and not has_append:
                res_list.append(res)
                res = ""
                has_append = True
        if tr == "[":
            is_emoji = True
        elif tr == "]":
            is_emojiend = True
            emoji_count += 1

        # 如果上一个是]
        if is_emojiend:
            is_emoji = False
            is_emojiend = False

        if not is_emoji:
            tr_pinyin = lazy_pinyin(tr)[0]
            if tr_pinyin in PY_MAP:
                # tr = r"[CQ:emoji,id=" + PY_MAP[tr_pinyin] + "]"
                tr = PY_MAP[tr_pinyin]
                emoji_count += 1

        res = res + tr
    res_list.append(res)

    # 把%+%替换为+
    # res = res.replace(r"%+%", "+")
    # print (res)

    for res in res_list:
        send_group_msg(res, data["group_id"])
        send_group_msg("芜湖", data["group_id"])
        ah = r"[CQ:music,type=qq,id=213448650]"
        send_group_msg(ah, data["group_id"])
        send_group_msg("哈哈", data["group_id"])
