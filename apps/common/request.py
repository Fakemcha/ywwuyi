import ssl
import string
import time
import urllib.parse
import urllib.request

import requests
from ywwuyi import config

from common.logs import write_test_log


def request_by_url(url, useProxy=False, returnContent=True, sleep=0):
    """
    :param url:
    :param useProxy: 是否使用代理
    :param returnContent: 是否返回内容，否则返回True/False
    :return:
    """
    if "https://" in url:
        ssl._create_default_https_context = ssl._create_unverified_context

    if useProxy:
        proxies = config.proxies
    else:
        proxies = {}

    op = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
    urllib.request.install_opener(op)

    if int(sleep) > 0:
        time.sleep(int(sleep))
    request = urllib.request.Request(urllib.parse.quote(url, safe=string.printable), headers=config.headers)
    for i in range(config.request_retry_times):
        try:
            resopen = urllib.request.urlopen(request, timeout=config.request_timeout)
        except Exception as e:
            if i < (config.request_retry_times - 1):
                continue
            else:
                write_test_log("Error:urlopen", filename="request_error.log")
                write_test_log(str(url), filename="request_error.log")
                write_test_log(str(e.__traceback__.tb_frame.f_globals['__file__']), filename="request_error.log")
                write_test_log(str(e.__traceback__.tb_lineno), filename="request_error.log")
                write_test_log(str(type(e)), filename="request_error.log")
                write_test_log(str(e), filename="request_error.log")
                return False
        break

    if returnContent:
        try:
            response = resopen.read()
            return response
        except Exception as e:
            write_test_log("Error:read", filename="request_error.log")
            write_test_log(str(url), filename="request_error.log")
            write_test_log(str(e.__traceback__.tb_frame.f_globals['__file__']), filename="request_error.log")
            write_test_log(str(e.__traceback__.tb_lineno), filename="request_error.log")
            write_test_log(str(type(e)), filename="request_error.log")
            write_test_log(str(e), filename="request_error.log")
            return False
    else:
        return True


def post_by_url(url, data):
    r = requests.post(url, data=data)
    return r
