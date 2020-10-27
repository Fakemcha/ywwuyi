import datetime
import time
import string
import json
import random

from common.request import request_by_url
from urllib.parse import quote

from ywwuyi.cqrequest import send_group_msg
from ywwuyi.cqcode import parse_image

def news(data, type):
    #type top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
    group_id = data["group_id"]
    url = "http://v.juhe.cn/toutiao/index?type={}&key=c82eab2deb6d6d1a84eac0f27a0cf666".format(str(type))
    quote_url = quote(url, safe=string.printable)
    request_res = request_by_url(quote_url)
    request_dict = json.loads(request_res)
    news_data = request_dict["result"]["data"]
    print(news_data)
    msg = ""
    show_count = 3
    if len(news_data) < show_count:
        send_group_msg("错误：返回的新闻数量太少辣", group_id)
    #生成n个随机数
    random_numbers = []
    while(True):
        random_number = random.randint(0, len(news_data))
        if not random_number in random_numbers:
            random_numbers.append(random_number)
        if len(random_numbers) == show_count:
            break

    for random_number in random_numbers:
        news_title = news_data[random_number]["title"]
        news_date = news_data[random_number]["date"]
        news_author_name = news_data[random_number]["author_name"]
        news_url = news_data[random_number]["url"]
        news_pic = news_data[random_number]["thumbnail_pic_s"]
        print(news_pic)
        msg += "{}: {}\n{}\n{}\n{}\n\n".format(news_author_name, news_title, news_date, news_url, parse_image(news_pic))
    send_group_msg(msg, group_id)