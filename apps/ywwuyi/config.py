import os
import settings
from ywwuyi.cqcode import parse_at


# robot_id = 2292262388
robot_id = 3197335618
# coolq or mirai
qq_proxy = "mirai"
# mirai_interface_url = "http://ywwuyi.cc:1571/"
mirai_interface_url = "http://127.0.0.1:1552/"
mirai_auth_key = "poi233333"


request_url = "http://172.17.0.2:5700/"
request_timeout = 30
request_retry_times = 3

qq_cache_path = os.path.join(settings.PROJECT_DIR, 'public', 'static', 'qqcache')
# qq_cache_url = "http://106.54.129.208/static/qqcache/"
qq_cache_url = "http://127.0.0.1:801/static/qqcache/"
cq_cache_path = os.path.join(settings.PROJECT_DIR, 'public', 'static', 'cqcache')

headers = {
        "user-agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

proxies = {
    'https': 'https://192.168.8.128:1080',
    'http': 'http://192.168.8.128:1080'
}
