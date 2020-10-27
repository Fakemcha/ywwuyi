import json
import string
import urllib.request
import urllib.parse
from ywwuyi import config
from common.request import request_by_url


def send_private_msg(message, user_id):
    """
    :param message:
    :param user_id:
    :return:
    """
    arguments = {
        "message": str(message),
        "user_id": str(user_id),
    }

    url = config.request_url + "send_private_msg?" + urllib.parse.urlencode(arguments)
    # request_by_url(url, returnContent=False)
    result = json.loads(request_by_url(url, returnContent=True).decode("utf-8"))
    return result


def send_group_msg(message, group_id):
    """
    :param message:
    :param group_id:
    :return:
    """
    arguments = {
        "message": str(message),
        "group_id": str(group_id),
    }

    url = config.request_url + "send_group_msg?" + urllib.parse.urlencode(arguments)
    result = json.loads(request_by_url(url, returnContent=True).decode("utf-8"))
    return result


def delete_msg(message_id):
    """
    :param message_id:
    :return:
    """
    arguments = {
        "message_id": message_id,
    }
    url = config.request_url + "delete_msg?" + urllib.parse.urlencode(arguments)
    result = json.loads(request_by_url(url, returnContent=True).decode("utf-8"))
    return result


def get_group_member_info(group_id, user_id):
    """
    :param group_id:
    :param user_id:
    :return:
    """
    arguments = {
        "group_id": str(group_id),
        "user_id": str(user_id),
        "no_cache": True,
    }
    url = config.request_url + "get_group_member_info?" + urllib.parse.urlencode(arguments)
    res = json.loads(str(request_by_url(url, returnContent=True), encoding="utf-8"))
    # print(str(res["data"]["card"], encoding="utf-8"))
    return res


def get_group_info(group_id):
    """
    :param group_id:
    :return:
    """
    arguments = {
        "group_id": str(group_id),
        "no_cache": True,
    }
    url = config.request_url + "get_group_info?" + urllib.parse.urlencode(arguments)
    print("url:" + url)
    res = json.loads(str(request_by_url(url, returnContent=True), encoding="utf-8"))
    print("res:")
    print(res)
    # print(str(res["data"]["card"], encoding="utf-8"))
    return res


def ban(group_id, user_id, seconds):
    """
    :param group_id:
    :return:
    """
    arguments = {
        "group_id": str(group_id),
        "user_id": str(user_id),
        "duration": str(seconds),
    }
    url = config.request_url + "set_group_ban?" + urllib.parse.urlencode(arguments)
    print("url:" + url)
    res = json.loads(str(request_by_url(url, returnContent=True), encoding="utf-8"))
    print("res:")
    print(res)
    # print(str(res["data"]["card"], encoding="utf-8"))
    return res