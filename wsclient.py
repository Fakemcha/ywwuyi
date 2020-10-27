# -*- coding: UTF-8 -*-
import os
import sys
# 加路径
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apps')
sys.path.append(BASE_DIR)
import time
from ywwuyi.miraiwebsocket import listen_mirai

if __name__ == '__main__':
    # 循环 启动mirai ws
    while True:
        listen_mirai()
        time.sleep(10)
    # pass