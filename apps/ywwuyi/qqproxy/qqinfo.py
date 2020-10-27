# -*- coding: UTF-8 -*-
import json
import string
import urllib.request
import urllib.parse
from ywwuyi import config
from ywwuyi.config import qq_proxy,mirai_interface_url
from common.request import request_by_url


def get_group_nick(group_id, user_id):
    """
    :param group_id:
    :param user_id:
    :return:
    """
    if qq_proxy == "mirai":
        from ywwuyi.qqproxy.mirai import mirai_session
        arguments = {
            "sessionKey": mirai_session.get_session_key(),
            "target": int(group_id),
            "memberId": int(user_id)
        }
        url = mirai_interface_url + "memberInfo?" + urllib.parse.urlencode(arguments)
        res = json.loads(str(request_by_url(url, returnContent=True), encoding="utf-8"))
        print("x" * 60)
        print(res)
        print("x" * 60)
        return res["name"]
    elif qq_proxy == "coolq":
        pass
        arguments = {
            "group_id": str(group_id),
            "user_id": str(user_id),
            "no_cache": True,
        }
        url = config.request_url + "get_group_member_info?" + urllib.parse.urlencode(arguments)
        res = json.loads(str(request_by_url(url, returnContent=True), encoding="utf-8"))
        # print(str(res["data"]["card"], encoding="utf-8"))
        return res
    else:
        return None