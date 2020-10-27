# -*- coding: UTF-8 -*-
import time
from common.chrome import request_by_chrome
from bs4 import BeautifulSoup
from ywwuyi.cqrequest import send_group_msg
from common.logs import write_test_log

def get_3300x():
    group_id = "92172618"
    url = r"https://item.jd.com/100012894962.html"
    # url = r"https://item.jd.com/100004995955.html"
    html = request_by_chrome(url)
    soup = BeautifulSoup(html, 'html.parser')
    all_a = soup.findAll("a", {'id': 'btn-notify'})
    if len(all_a) == 1:
        element = all_a[0]
        element.string
        if element.string == "到货通知":
            style = element['style']
            if "display:none;" in style:
                # 有货
                send_group_msg("amd 3300x 有货辣\n" + url, group_id)
                write_test_log(str(time.time()) + " 有货")
                pass
            else:
                # send_group_msg("无货", group_id)
                write_test_log(str(time.time()) + " 无货")
                pass
        else:
            pass
    else:
        pass
