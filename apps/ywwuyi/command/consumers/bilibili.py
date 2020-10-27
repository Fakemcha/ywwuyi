# -*- coding: UTF-8 -*-
import os
import json
from PIL import Image
from apps.settings import TMP_DIR
from common.request import request_by_url
from ywwuyi.cqrequest import send_group_msg
from ywwuyi.models.bilibili_subscription import BilibiliSubscription
from ywwuyi.qqproxy.sendmessage import SendQQMessage
from ywwuyi.config import qq_cache_path, qq_cache_url


def cache_face(face_url):
    face_filename = face_url[face_url.rindex("/") + 1:]
    if not os.path.exists(qq_cache_path + "/" + face_filename):
        res = request_by_url(face_url)
        tmp_pic_filepath = TMP_DIR + "/" + face_filename
        with open(tmp_pic_filepath, mode="wb") as f:
            f.write(res)
        # resize_pic(tmp_pic_filepath)
        ori_img = Image.open(tmp_pic_filepath)
        new_img = ori_img.resize((100, 100), Image.ANTIALIAS)
        new_img = new_img.convert('RGB')
        new_img.save(qq_cache_path + "/" + face_filename)
    face_image_url = qq_cache_url + face_filename
    return face_image_url


def share_xcx(data):
    """分享小程序"""
    group_id = data["group_id"]
    message = data["message"]
    # print(message)
    # print("="*50)
    # print(str(message).replace(r"&#44;", ","))
    _start = str(message).find("content=") + 8
    _end = str(message).find(",title=")
    # print(str(_end))
    # print(message[:_end])
    content = str(message[_start:_end]).replace(r"&#44;", ",")
    # print(content)
    content_dict = json.loads(content)
    if "detail_1" in content_dict:
        appid = int(content_dict["detail_1"]["appid"])
    elif "music" in content_dict:
        appid = int(content_dict["music"]["appid"])
    if appid == 1109937557:
        # bilibili
        share_url = content_dict["detail_1"]["qqdocurl"]
        title = content_dict["detail_1"]["desc"]
        if str(share_url).find(r"?") != -1:
            url = share_url[:str(share_url).find(r"?")]
        else:
            url = share_url
        msg = "来自[哔哩哔哩]分享\n{}\n{}".format(title, url)
        send_group_msg(msg, group_id)
    elif appid == 1110081493:
        # 知乎
        share_url = content_dict["detail_1"]["qqdocurl"]
        title = content_dict["detail_1"]["desc"]
        if str(share_url).find(r"?") != -1:
            url = share_url[:str(share_url).find(r"?")]
        else:
            url = share_url
        msg = "来自[知乎]分享\n{}\n{}".format(title, url)
        send_group_msg(msg, group_id)
    elif appid == 100495085:
        # 网易云音乐
        share_url = content_dict["music"]["jumpUrl"]
        title = "{} - {}".format(content_dict["music"]["title"], content_dict["music"]["desc"])
        if str(share_url).find(r"?") != -1:
            url = share_url[:str(share_url).find(r"?")]
        else:
            url = share_url
        msg = "来自[网易云音乐]分享\n{}\n{}".format(title, url)
        send_group_msg(msg, group_id)
    print(content_dict)


def subscripbe(qqmessage):
    user_id = qqmessage.get_sender_id()
    group_id = qqmessage.get_group_id()
    content = qqmessage.get_content()
    if len(content.split(" ")) == 2:
        bilibili_id = content.split(" ")[1]
        if bilibili_id.isdigit():
            try:
                bilisub = BilibiliSubscription(user_id=user_id, group_id=group_id, bilibili_id=bilibili_id)
                bilisub.save()
                sqm = SendQQMessage()
                sqm.add_group_id(group_id)
                sqm.add_content("订阅成功")
                sqm.send()
            except Exception:
                sqm = SendQQMessage()
                sqm.add_group_id(group_id)
                sqm.add_content("已经订阅过惹")
                sqm.send()
        else:
            sqm = SendQQMessage()
            sqm.add_group_id(group_id)
            sqm.add_content("订阅失败，目前只支持ID")
            sqm.send()
    else:
        sqm = SendQQMessage()
        sqm.add_group_id(group_id)
        sqm.add_content("订阅失败，格式错误")
        sqm.send()


def search_user(qqmessage):
    group_id = qqmessage.get_group_id()
    content = qqmessage.get_content()
    if len(content.split(" ")) == 2:
        keyword = content.split(" ")[1]
        url = r"https://api.bilibili.com/x/web-interface/search/all/v2?keyword={}&page=1&pagesize=1&search_type=bili_user&order=".format(keyword)
        res = json.loads(request_by_url(url).decode(encoding="utf-8"))
        print(res)
        for r in res["data"]["result"]:
            if r["result_type"] == "bili_user":
                # print(r["data"])
                if len(r["data"]) == 0:
                    sqm = SendQQMessage()
                    sqm.add_group_id(group_id)
                    sqm.add_content("没有搜索到{}".format(keyword))
                    sqm.send()
                    return
                else:
                    user_res = r["data"][0]
        print(user_res)
        face_image_url = cache_face("https:" + user_res["upic"])
        mid = user_res["mid"]
        name = user_res["uname"]
        sign = user_res["usign"]
        fans_num = user_res["fans"]
        videos_num = user_res["videos"]

        sqm = SendQQMessage()
        sqm.add_group_id(group_id)
        sqm.add_image(face_image_url)
        sqm.add_content(name + " ")
        sqm.add_content("ID: {}".format(mid) + "\n")
        sqm.add_content("签名: {}".format(sign) + "\n")
        sqm.add_content("稿件: {}".format(videos_num))
        sqm.add_content(" 粉丝: {}".format(fans_num))
        sqm.send()
    else:
        sqm = SendQQMessage()
        sqm.add_group_id(group_id)
        sqm.add_content("订阅失败，格式错误")
        sqm.send()
