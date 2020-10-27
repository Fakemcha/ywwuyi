# -*- coding: UTF-8 -*-
import json
import random
from ywwuyi.config import cq_cache_path
from ywwuyi.qqproxy.sendmessage import SendQQMessage


def wxz(qqmessage):
    if qqmessage.is_group_message():
        group_id = qqmessage.get_group_id()
        WXZ_PATH = str(cq_cache_path) + r"/wxz.json"
        with open(WXZ_PATH, mode="r") as f:
            wxz_list = json.loads(f.read())
        wxz_str = wxz_list[random.randint(0, len(wxz_list) - 1)]
        sqm = SendQQMessage()
        sqm.add_group_id(group_id)
        sqm.add_content(wxz_str)
        sqm.send()


def add_wxz(qqmessage):
    content = qqmessage.get_content()
    if "肖战" in content:
        WXZ_PATH = str(cq_cache_path) + r"/wxz.json"
        with open(WXZ_PATH, mode="r") as f:
            wxz_list = json.loads(f.read())
        wxz_list.append(content)
        with open(WXZ_PATH, mode="w") as f:
            f.write(json.dumps(list(set(wxz_list)), ensure_ascii=False))
