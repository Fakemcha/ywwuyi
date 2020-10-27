from ywwuyi.timedtask.pattern import TimedtaskPattern
from .consumers.test import ywwuyiQuotesTest
# from ywwuyi.timedtask.consumers.jd import get_3300x
from ywwuyi.timedtask.consumers.bilibili import parse_bilibili


timedtaskPatterns = [
    # TimedtaskPattern("ywwuyi1", {"seconds": 10}, ywwuyiQuotesTest),
    # TimedtaskPattern("ywwuyi2", {"seconds": 10}, ywwuyiQuotesTest),
    # TimedtaskPattern("ywwuyi3", {"seconds": 10}, ywwuyiQuotesTest),
    # TimedtaskPattern("ywwuyi3", {"seconds": 10}, ywwuyiQuotesTest),
    # TimedtaskPattern("get_3300x", {"hours": 1}, get_3300x),
    TimedtaskPattern("bilibili", {"seconds": 180}, parse_bilibili)
]