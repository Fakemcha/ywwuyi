from common.logs import write_test_log
from .cqrequest import send_group_msg


def test(data):
    # write_test_log("你好", filename="test.log")

    send_group_msg("噔噔噔噔，收到信号了呢", data["group_id"])