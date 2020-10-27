# -*- coding: UTF-8 -*-
import os
import json
import time
from PIL import Image
from apps.settings import TMP_DIR
from common.request import request_by_url
from common.redis_connect import RedisConnect
from ywwuyi.qqproxy.sendmessage import SendQQMessage
from ywwuyi.config import qq_cache_path, qq_cache_url


rc = RedisConnect()


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


def cache_picture(picture_url):
    print(picture_url)
    picture_filename = picture_url[picture_url.rindex("/") + 1:]
    pic_filepath = qq_cache_path + "/" + picture_filename
    if not os.path.exists(pic_filepath):
        res = request_by_url(picture_url)
        with open(pic_filepath, mode="wb") as f:
            f.write(res)
        # resize_pic(tmp_pic_filepath)
    #     ori_img = Image.open(tmp_pic_filepath)
    #     new_img = ori_img.resize((100, 100), Image.ANTIALIAS)
    #     new_img = new_img.convert('RGB')
    #     new_img.save(qq_cache_path + "/" + face_filename)
    face_image_url = qq_cache_url + picture_filename
    return face_image_url

def resize_pic(pic_file_path, x=100, y=100):
    pic_filename = pic_file_path[pic_file_path.rindex("/") + 1:]
    ori_img = Image.open(pic_file_path)
    new_img = ori_img.resize((x, y), Image.ANTIALIAS)
    new_img = new_img.convert('RGB')
    new_img.save(qq_cache_path + "/" + pic_filename)


def download_pic(url):
    pic_filename = url[url.rindex("/") + 1:]
    res = request_by_url(url)
    tmp_pic_filepath = TMP_DIR + "/" + pic_filename
    with open(tmp_pic_filepath, mode="wb") as f:
        f.write(res)
    resize_pic(tmp_pic_filepath)


def get_dynamic(bilibili_id):
    # print("请求动态{}".format(bilibili_id))
    url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid={}offset_dynamic_id=0".format(str(bilibili_id))
    # print("URL:{}".format(url))
    res = request_by_url(url, returnContent=True)
    # print(res)
    # with open(r"/home/bilibili", mode="wb") as f:
    #     f.write(res)
    if res:
        res = res.decode(encoding="utf-8")
        return json.loads(res)
    else:
        return None


def parse_bilibili():
    from ywwuyi.models.bilibili_subscription import BilibiliSubscription
    print("请求bilibili动态\n")
    with open("/home/timetasks", mode="a+") as f:
        f.write("{} 请求bilibili动态\n".format(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())))
    # 所有订阅的ID
    bilibili_subscriptions = BilibiliSubscription.objects.values("bilibili_id").distinct()
    for bilibili_subscription in bilibili_subscriptions:
        bilibili_id = bilibili_subscription["bilibili_id"]
        # 请求bilibili接口
        res = get_dynamic(bilibili_id)
        if not res:
            continue
        cards = res["data"]["cards"]
        for i in cards:
            card = json.loads(i["card"])
            # 有新发布的视频
            if "aid" in card:
                # print("=" * 50)
                # print(card)
                # print("=" * 50)
                # redis缓存
                redis_key = "1" + str(card["aid"]) + str(card["ctime"])
                redis_result = rc.get(redis_key)
                # if not redis_result or redis_key == "13720482201599362148":
                if not redis_result:
                    video_url = "https://www.bilibili.com/video/av{}".format(card["aid"])
                    # 获取头像
                    face_image_url = cache_face(card["owner"]["face"])
                    name = card["owner"]["name"]
                    title = card["title"]
                    timestamp = card["ctime"]
                    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                    sqm = SendQQMessage()
                    # 获取订阅到当前UP的群号
                    bss = BilibiliSubscription.objects.filter(bilibili_id=bilibili_id).values("group_id").distinct()
                    for bs in bss:
                        group_id = bs["group_id"]
                        sqm.add_group_id(group_id)
                    sqm.add_image(face_image_url)
                    sqm.add_content(name + "\n")
                    sqm.add_content(time_str + "\n")
                    sqm.add_content(title + "\n")
                    sqm.add_content(card["dynamic"] + "\n")
                    sqm.add_content(video_url + "\n")
                    sqm.send()
                    rc.set(redis_key, 1)
            # 普通动态
            elif "item" in card and "uid" in card["item"] and "timestamp" in card["item"]:
                # print("=" * 50)
                # print(card)
                # print("=" * 50)
                # redis缓存
                redis_key = "2" + str(card["item"]["uid"]) + str(card["item"]["timestamp"])
                redis_result = rc.get(redis_key)
                if not redis_result:
                    # 获取头像
                    face_image_url = cache_face(card["user"]["face"])
                    name = card["user"]["uname"]
                    timestamp = card["item"]["timestamp"]
                    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                    content = card["item"]["content"]
                    sqm = SendQQMessage()
                    sqm.add_image(face_image_url)
                    sqm.add_content(name + "\n")
                    sqm.add_content(time_str + "\n")
                    sqm.add_content(content + "\n")
                    # 转发动态，获取源动态
                    if "origin" in card:
                        origin = json.loads(card["origin"])
                        print("origin:")
                        print(origin)
                        print("==============================================")
                        # 转发文字动态
                        if "user" in origin:
                            # 转发别人的动态
                            if "name" in origin["user"]:
                                origin_name = origin["user"]["name"]
                                print("origin_name={}".format(origin_name))
                                origin_description = origin["item"]["description"]
                                print("origin_description={}".format(origin_description))
                                sqm.add_content("{}\n".format(origin_name))
                                sqm.add_content("{}\n".format(origin_description))
                                # 如果源动态有图片
                                if origin["item"]["pictures_count"] > 0:
                                    for picture in origin["item"]["pictures"]:
                                        img_src = picture["img_src"]
                                        print(img_src)
                                        picture_url = cache_picture(img_src)
                                        sqm.add_image(picture_url)
                            # 转发自己的动态
                            elif "uname" in origin["user"]:
                                origin_name = origin["user"]["uname"]
                                print("origin_name={}".format(origin_name))
                                origin_description = origin["item"]["content"]
                                print("origin_description={}".format(origin_description))
                                sqm.add_content("{}\n".format(origin_name))
                                sqm.add_content("{}\n".format(origin_description))
                        # 转发视频动态
                        elif "owner" in origin:
                            origin_name = origin["owner"]["name"]
                            origin_face_image_url = cache_face(origin["owner"]["face"])
                            origin_title = origin["title"]
                            origin_desc = origin["desc"]
                            origin_video_url = "https://www.bilibili.com/video/av{}".format(origin["aid"])
                            sqm.add_image(origin_face_image_url)
                            sqm.add_content(origin_name + "\n")
                            sqm.add_content(origin_title + "\n")
                            sqm.add_content(origin_desc + "\n")
                            sqm.add_content(origin_video_url)
                        # 转发文章动态
                        elif "author" in origin:
                            origin_name = origin["author"]["name"]
                            origin_face_image_url = cache_face(origin["author"]["face"])
                            origin_ctime_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(origin["ctime"]))
                            origin_title = origin["title"]
                            origin_article = "https://www.bilibili.com/read/cv{}".format(str(origin["id"]))
                            sqm.add_image(origin_face_image_url)
                            sqm.add_content(origin_name + "\n")
                            sqm.add_content(origin_ctime_str + "\n")
                            sqm.add_content(origin_title + "\n")
                            sqm.add_content(origin_article)

                    # 获取订阅到当前UP的群号
                    bss = BilibiliSubscription.objects.filter(bilibili_id=bilibili_id).values("group_id").distinct()
                    for bs in bss:
                        group_id = bs["group_id"]
                        sqm.add_group_id(group_id)

                    sqm.send()
                    rc.set(redis_key, 1)
        time.sleep(1)


