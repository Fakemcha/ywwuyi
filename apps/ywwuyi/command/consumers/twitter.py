import datetime
import time
import os
from bs4 import BeautifulSoup
from common.request import request_by_url
from common.logs import write_test_log
from ywwuyi import config
from ywwuyi.cqrequest import send_group_msg
from ywwuyi import cqcode


def cutStr(str, tr):
    n = str.find(tr, 0)
    if n != -1:
        return cutStr(str[n+1:], tr)
    else:
        return str


def twitter(data):
    message = data["message"]
    author = message.split(' ')[1]
    nickname = author

    url = r"https://twitter.com/search?q=(from%3A{})%20until%3A{}%20since%3A{}&src=typed_query".format(author, str(
        datetime.date.today() + datetime.timedelta(days=1)), str(datetime.date.today() - datetime.timedelta(days=1)))

    response = request_by_url(url, useProxy=True)
    if not response:
        send_group_msg("请求推特失败", data["group_id"])
        return
    soup = BeautifulSoup(response, 'lxml')
    res_list = []
    res_content_list = soup.findAll(attrs={'class', r'content'})
    is_send_require_photo = False
    require_photo_count = 0
    for res_content in res_content_list:
        content_dict = {}
        # 解析推特内容
        res_text = res_content.findAll(attrs={'class', r'js-tweet-text-container'})[0].find('p').get_text()
        content_dict["text"] = res_text
        # 解析时间
        res_date = \
        res_content.findAll(attrs={'class', r'tweet-timestamp js-permalink js-nav js-tooltip'})[0].findAll('span')[
            0].get("data-time")
        res_date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(res_date)))
        content_dict["date"] = res_date_str
        # 解析图片
        photoContainer_list = res_content.findAll(attrs={'class', r'AdaptiveMedia-photoContainer js-adaptive-photo '})
        photoContainer_list = photoContainer_list + res_content.findAll(
            attrs={'class', r'AdaptiveMedia-photoContainer js-adaptive-photo'})
        res_photo_list = []
        # 如果推文有带图片
        if len(photoContainer_list) > 0:
            for photoContainer in photoContainer_list:
                photo_url = photoContainer.findAll('img')[0].get("src")
                photo_name = cutStr(photo_url, r"/")
                if not os.path.exists(config.cq_cache_path + r"/" + photo_name):
                    # 请求并保存图片
                    require_photo_count += 1
                    if require_photo_count == 3:
                        send_group_msg("WDNMD，怎么有这么多张图片", data["group_id"])
                    if require_photo_count == 6:
                        msg = "[CQ:emoji,id=128102]佛了，" + nickname + "能少发点图片[CQ:emoji,id=128052]"
                        send_group_msg(msg, data["group_id"])
                    if not is_send_require_photo:
                        send_group_msg("正在获取推文中的图片...", data["group_id"])
                        is_send_require_photo = True
                    print("请求图片:" + photo_name)
                    photo_byte = request_by_url(photo_url, useProxy=True)
                    photo_file_path = str(config.cq_cache_path) + r"/" + photo_name
                    with open(photo_file_path, 'wb') as f:
                        f.write(photo_byte)
                res_photo_list.append(photo_name)
        content_dict["photos"] = res_photo_list
        res_list.append(content_dict)

    # write_test_log("list:" + str(res_list))
    if len(res_list) > 0:
        #排序
        for i in range(len(res_list)):
            for j in range(len(res_list) - 1 - i):
                if res_list[j + 1]["date"] > res_list[j]["date"]:
                    res_list[j + 1],res_list[j] = res_list[j],res_list[j + 1]
    else:
        send_group_msg("{}最近没有发布推特".format(nickname), data["group_id"])
        return
    # write_test_log("list_paixu:" + str(res_list))

    qq_str = "{}发布了{}条推特:".format(nickname, len(res_list))
    for i in range(len(res_list)):
        if i > 0:
            qq_str = qq_str + "\n" + "-" * 100
        qq_str = qq_str + "\n"
        qq_str = qq_str + res_list[i]["date"] + "\n"
        qq_str = qq_str + res_list[i]["text"]
        if len(res_list[i]["photos"]) > 0:
            for j in range(len(res_list[i]["photos"])):
                qq_str = qq_str + cqcode.parse_image("http://mqmmw.qftal.com/static/cqcache/" + res_list[i]["photos"][j])

    send_group_msg(qq_str, data["group_id"])