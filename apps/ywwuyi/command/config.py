from .pattern import CommandPattern
# from ywwuyi.config import robot_id
# from ywwuyi.cqcode import parse_at, parse_image
# from .consumers.twitter import twitter
from .consumers.nmsl import nmslTransilate
# from .consumers.ywwuyiquotes import ywwuyiQuotes
# from .consumers.test import send_task_name, qidong, del_task
from .consumers.dragonking import dragonking
# from .consumers.pihua import pihua
# from .consumers.language import ylzz, gxl, sbbz, npy, sbbc, yxh, ecy, jrsy, ldsy, tgrj
from .consumers.history import history
from .consumers.language import ylzz, sbbc
# from .consumers.news import news
# from .consumers.shitessay import get_shit_essay
# from .consumers.bilibili import share_xcx
from .consumers.repeater import repeat
from .consumers.wxz import wxz, add_wxz
from .consumers.cgc import caigemin, gemin
from .consumers.magnet import magnet
# from ywwuyi.games.guess_keyword import forbidden_words_game

from ywwuyi.command.consumers.future_event import future_event
# from apps.bilibili import parse_bilibili
from .consumers.bilibili import subscripbe, search_user


# func_mapping = {
#     "ywwuyiQuotes": ywwuyiQuotes,
#     "twitter": twitter,
#     "nmslTransilate": nmslTransilate,
#     "qidong": qidong,
#     "send_task_name": send_task_name,
#     "del_task": del_task,
# }

commandPatterns = [
    # CommandPattern('^' + parse_at(robot_id) + '$', ywwuyiQuotes),
    CommandPattern('', repeat, isEnd=False),
    CommandPattern('^未来$', future_event.check),

    CommandPattern('^#', add_wxz),
    CommandPattern('^无肖战$', wxz),
    # CommandPattern('^测试', parse_bilibili),
    CommandPattern('^订阅UP ', subscripbe),
    CommandPattern('^搜索UP ', search_user),
    CommandPattern('^猜歌名$', caigemin),
    CommandPattern('^歌名$', gemin),

    # CommandPattern(parse_at(robot_id), ywwuyiQuotes),
    # CommandPattern('^测试', test),


    # CommandPattern('^[CQ:at,qq=' + ".*" + ']$', forbidden_words_game.check_powder),
    # CommandPattern('^[CQ:rich', share_xcx),

    # CommandPattern('^禁语 ', forbidden_words_game.my_forbidden_word),
    # CommandPattern('^禁语重置$', forbidden_words_game.make_forbidden_words, private=[463705592]),

    CommandPattern('^影流之主$', ylzz),
    CommandPattern('^[0-9a-e]{40}$', magnet),
    # CommandPattern('^推文', twitter),
    # CommandPattern('^该歇了$', gxl),
    # CommandPattern('女朋友', npy),
    # CommandPattern('^傻逼部长$', sbbz),
    # CommandPattern('^煞笔部长$', sbbz),
    # CommandPattern('^来点二次元', ecy),
    # CommandPattern('^今日爽语$', jrsy),
    # CommandPattern('^来点爽语$', ldsy),

    # CommandPattern('^舔狗日记$', tgrj),
    CommandPattern('^抽象翻译', nmslTransilate),
    # CommandPattern('^什么是', yxh, group=[92172618, 963908620, 532799508]),
    # CommandPattern('^如何评价', get_shit_essay, group=[92172618, 963908620, 532799508]),
    # CommandPattern('^任务启动$', qidong),
    # CommandPattern('^任务列表$', send_task_name),
    # CommandPattern('^删除任务', del_task),




    # CommandPattern('^联调分配 ', ltassignation.get_id),
    # CommandPattern('^查询分配 ', ltassignation.search),
    # CommandPattern('^已分配企业', ltassignation.get_info),
    # CommandPattern('^删除联调分配 ', ltassignation.delete, private=[2079215102]),
    # CommandPattern('^删除任务', del_task),

    CommandPattern('^今日龙王$', dragonking, private=None, group=["*"], kwargs={"day": "today"}),
    CommandPattern('^昨日龙王$', dragonking, private=None, group=["*"], kwargs={"day": "yesterday"}),
    # CommandPattern('^今日批话$', pihua, private=None, group=["*"], kwargs={"day": "today"}),
    # CommandPattern('^昨日批话$', pihua, private=None, group=["*"], kwargs={"day": "yesterday"}),
    # CommandPattern('^本周批话$', pihua, private=None, group=["*"], kwargs={"day": "week"}),
    # CommandPattern('^上周批话$', pihua, private=None, group=["*"], kwargs={"day": "lastweek"}),
    # CommandPattern('^本月批话$', pihua, private=None, group=["*"], kwargs={"day": "month"}),
    # CommandPattern('^上个月批话$', pihua, private=None, group=["*"], kwargs={"day": "lastmonth"}),
    CommandPattern('^历史上的今天$', history, private=None, group=["*"]),

    # CommandPattern('^国内新闻$', news, private=None, group=["*"], kwargs={"type": "guonei"}),
    # CommandPattern('^国际新闻$', news, private=None, group=["*"], kwargs={"type": "guonei"}),
    # CommandPattern('^科技新闻$', news, private=None, group=["*"], kwargs={"type": "guonei"}),


    CommandPattern('', sbbc, isEnd=False),
    # CommandPattern('', forbidden_words_game.check_keyword),
]