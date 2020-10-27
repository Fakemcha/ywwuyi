# -*- coding: UTF-8 -*-
import os
import json
import time
from PIL import Image
from settings import TMP_DIR
from common.request import request_by_url
from ywwuyi.qqproxy.sendmessage import SendQQMessage
from ywwuyi.config import qq_cache_path, qq_cache_url

# from common.redis_connect import RedisConnect
# from ywwuyi.models.bilibili_subscription import BilibiliSubscription

# rc = RedisConnect()


# def get_groupid_by_bilibiliid(bilibili_id):
#     bs = BilibiliSubscription.objects.filter(bilibili_id=bilibili_id).values("group_id").distinct()
#     for i in bs:
#         print("x"*50)
#         print(i["group_id"])
#         print("x"*50)


def download_pic(url):
    pic_filename = url[url.rindex("/") + 1:]
    res = request_by_url(url)
    tmp_pic_filepath = TMP_DIR + "/" + pic_filename
    with open(tmp_pic_filepath, mode="wb") as f:
        f.write(res)
    resize_pic(tmp_pic_filepath)


def resize_pic(pic_file_path, x=100, y=100):
    pic_filename = pic_file_path[pic_file_path.rindex("/") + 1:]
    ori_img = Image.open(pic_file_path)
    new_img = ori_img.resize((x, y), Image.ANTIALIAS)
    new_img = new_img.convert('RGB')
    new_img.save(qq_cache_path + "/" + pic_filename)


def get_dynamic(bilibili_id):
    url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid={}offset_dynamic_id=0".format(str(bilibili_id))
    res = request_by_url(url, returnContent=True)
    # print(res)
    # with open(r"/home/bilibili", mode="wb") as f:
    #     f.write(res)
    res = res.decode(encoding="utf-8")
    return json.loads(res)


def decode_bilibili():
    with open(r"/home/bilibili", mode="rb") as f:
        res = f.read()
    s = res.decode(encoding="utf-8")
    # print(s)
    res_dict = json.loads(s)
    # print(res_dict)
    return res_dict


# def parse_bilibili(data):
#     # 所有订阅的ID
#     bilibili_subscriptions = BilibiliSubscription.objects.values("bilibili_id").distinct()
#     for bilibili_subscription in bilibili_subscriptions:
#         bilibili_id = bilibili_subscription["bilibili_id"]
#         # 请求bilibili接口
#         res = get_dynamic(bilibili_id)
#         cards = res["data"]["cards"]
#         for i in cards:
#             card = json.loads(i["card"])
#             # 有新发布的视频
#             if "aid" in card:
#                 # redis缓存
#                 redis_key = str(card["aid"]) + str(card["ctime"])
#                 redis_result = rc.get(redis_key)
#                 if not redis_result:
#                     # 获取订阅到当前UP的群号
#                     bss = BilibiliSubscription.objects.filter(bilibili_id=bilibili_id).values("group_id").distinct()
#                     for bs in bss:
#                         group_id = bs["group_id"]
#                         print(card)
#                         rc.set(redis_key, 1)
#                         video_url = "https://www.bilibili.com/video/av{}".format(card["aid"])
#                         face_image_url = card["owner"]["face"]
#                         face_pic_file_name = face_image_url[face_image_url.rindex("/") + 1:]
#                         # 没有请求过这张头像
#                         if not os.path.exists(qq_cache_path + "/" + face_pic_file_name):
#                             download_pic(face_image_url)
#
#                         face_image_url = qq_cache_url + face_pic_file_name
#                         name = card["owner"]["name"]
#                         title = card["title"]
#                         timestamp = card["ctime"]
#                         time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
#                         sqm = SendQQMessage()
#                         sqm.add_group_id(group_id)
#                         sqm.add_image(face_image_url)
#                         sqm.add_content(name + "\n")
#                         sqm.add_content(time_str + "\n")
#                         sqm.add_content(title + "\n")
#                         sqm.add_content(card["dynamic"] + "\n")
#                         sqm.add_content(video_url + "\n")
#                         sqm.send()


def bilibili_search(keyword):
    url = "https://api.bilibili.com/x/web-interface/search/type?context=&keyword={}&page=1&order=&category_id=&duration=&user_type=&order_sort=&tids_1=&tids_2=&search_type=bili_user&changing=mid&__refresh__=true&__reload__=false&_extra=&highlight=1&single_column=0&jsonp=jsonp&callback=__jp5".format(keyword)
    url = r"https://api.bilibili.com/x/web-interface/search/type?context=&keyword=%E6%B3%BD%E9%87%8E%E8%9E%B3%E8%9E%82&page=1&order=&category_id=&duration=&user_type=&order_sort=&tids_1=&tids_2=&search_type=bili_user&changing=mid&__refresh__=true&__reload__=false&_extra=&highlight=1&single_column=0&jsonp=jsonp&callback=__jp5"
    url = r"https://api.bilibili.com/x/web-interface/search/all/v2?keyword=%E6%B3%BD%E9%87%8E%E8%9E%B3%E8%9E%82&page=1&pagesize=1&search_type=bili_user&order="
    url = r"https://api.bilibili.com/x/web-interface/search/all/v2?keyword=泽野螳螂&page=1&pagesize=1&search_type=bili_user&order="

    print(url)
    res = request_by_url(url)


    res = res.decode(encoding="utf-8")

    res = json.loads(res)
    # print(res["data"]["result"])
    for r in res["data"]["result"]:
        if r["result_type"] == "bili_user":
            print(r["data"])


if __name__ == '__main__':
    # bilibili_search("泽野螳螂")
    res = get_dynamic("332704117")
    # print(res["data"]["cards"])
    # print(res)

    for i in res["data"]["cards"]:
        card = json.loads(i["card"])
        print("=" * 50)
        print(card)
        print("~" * 50)
        if "origin" in card:
            origin = json.loads(card["origin"])
            print(origin)
            # print( origin["user"] )
            # print( origin["user"]["name"] )
        print("=" * 50)