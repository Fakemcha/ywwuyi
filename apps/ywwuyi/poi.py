import requests
import json
from ywwuyi.cqrequest import send_private_msg, send_group_msg


def handle_url(url):
    def method(data):
        r = requests.get(url, data)
        r.encoding = "utf-8"
        if r.status_code != 200:
            pass
        res_json = r.text
        res = json.loads(res_json)
        if not isinstance(res, dict):
            pass
        if not "message" in res:
            pass
        if "group_id" in res:
            message = res["message"]
            group_id = res["group_id"]
            send_group_msg(message, group_id)
        elif "private_id" in res:
            message = res["message"]
            user_id = res["user_id"]
            send_private_msg(message, user_id)
        else:
            pass
    return method