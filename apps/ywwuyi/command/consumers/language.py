import datetime
import random

from ywwuyi import cqcode
from ywwuyi import config
from ywwuyi.cqrequest import send_group_msg
from common.request import request_by_url
from ywwuyi.config import qq_cache_url
from ywwuyi.qqproxy.sendmessage import SendQQMessage
from ywwuyi.command.consumers.nmsl import nmsl_trasilate


def ylzz(qqmessage):
    # 影流之主
    group_id = qqmessage.get_group_id()
    # send_group_msg(cqcode.parse_image(r"http://mqmmw.qftal.com/static/img/4Y(I1OF`QP5_2MO3)AXX[NP.gif"), group_id)
    # send_group_msg(cqcode.parse_image("http://mqmmw.qftal.com/static/ywwuyiquotes/ylzz.gif"), group_id)
    # send_group_msg(cqcode.parse_image("http://172.17.0.1/static/ywwuyiquotes/ylzz.gif"), group_id)
    sqm = SendQQMessage()
    sqm.add_group_id(group_id)
    img_url = qq_cache_url + "ylzz.gif"
    sqm.add_image(img_url)
    sqm.send()



def gxl(data):
    # 该歇了
    group_id = data["group_id"]
    hour_now = int(datetime.datetime.now().hour)
    if hour_now >= 19 and hour_now <= 23:
        # send_group_msg(cqcode.parse_image("http://mqmmw.qftal.com/static/ywwuyiquotes/109.jpg"), group_id)
        send_group_msg(cqcode.parse_image("http://172.17.0.1/static/ywwuyiquotes/91.png"), group_id)


def sbbz(data):
    # 傻逼部长
    group_id = data["group_id"]
    send_group_msg(cqcode.parse_image("http://172.17.0.1/static/ywwuyiquotes/49.jpg"), group_id)


def npy(data):
    # 女朋友
    group_id = data["group_id"]
    send_group_msg(cqcode.parse_image("http://172.17.0.1/static/ywwuyiquotes/90.jpg"), group_id)


def sbbc(qqmessage):
    # group_id = data["group_id"]
    group_id = qqmessage.get_group_id()
    sender_id = qqmessage.get_sender_id()
    content = qqmessage.get_content()
    if (sender_id == 463705592 and group_id == 532799508) or (sender_id == 844266359 and group_id == 92172618):
        # if str(data["message"]).startswith("[CQ:") and str(data["message"]).endswith("]"):
        #     pass
        # else:
        #     msg = "「{}」： {}".format("班草", data["message"])
        #     send_group_msg(msg, group_id)
        for m in nmsl_trasilate(content):
            sqm = SendQQMessage()
            sqm.add_group_id(group_id)
            sqm.add_content(m)
            sqm.send()


def yxh(data):
    """营销号格式"""
    group_id = str(data["group_id"])
    message = str(data["message"])
    keyword = message.replace("什么是","",1).replace("?","").replace("？","")
    if keyword == "鸡哥":
        msg = "鸡哥相信大家都很熟悉，鸡哥其实就是一个憨批"
        send_group_msg(msg, group_id)
    else:
        msg = "{}相信大家都很熟悉，但是{}是怎么回事呢？下面就让爽哥带大家一起了解吧。{}，其实就是{}，大家可能会感到很惊讶，到底{}？但事实就是这样，爽哥也感到非常惊讶，那么这就是关于{}的事情了，大家有什么想法呢？欢迎在这里和大家一起讨论哦".format(
            keyword,
            keyword,
            keyword,
            keyword,
            message.replace("?", "").replace("？", ""),
            keyword
        )
        send_group_msg(msg, group_id)
    return


def ecy(data):
    """二次元图片"""
    group_id = str(data["group_id"])
    rand_int = random.randint(10000, 99999)
    picture_name = "example-{}.jpg".format(str(rand_int))
    picture_url = "https://www.thiswaifudoesnotexist.net/{}".format(picture_name)
    picture_byte = request_by_url(picture_url)
    picture_file_path = str(config.cq_cache_path) + r"/" + picture_name
    print(picture_url)
    with open(picture_file_path, 'wb') as f:
        f.write(picture_byte)
    send_group_msg(cqcode.parse_image("http://172.17.0.1/static/cqcache/" + picture_name), data["group_id"])


def jrsy(data):
    """今日爽语"""
    group_id = str(data["group_id"])
    msg = "我们这一生很短，我们终将会失去它，所以不妨大胆一点， 爱一个人，攀一座山，追一次梦，不妨大胆一点，有很多事没有答案。"
    send_group_msg(msg, group_id)


def ldsy(data):
    """来点爽语"""
    group_id = str(data["group_id"])
    msg_list = [
        "鱼肥果熟入我肚，下期节目大书库。",
        "图画里，龙不吟虎不啸，小小书童可笑可笑\n猛男寨，天不韦狗不叫，救救兄弟给点给点",
        "十口心思，思君思国思社稷\n两眼一黑，黑楼黑旗▇▇▇!",
        "所谓有趣的灵魂，实际上就是这个人的信息密度和知识层面，都远高于你，并愿意俯下身去听你说那毫无营养的废话和你交流，提出一些你没有听过的观点，颠覆了你短浅的想象力及三观。",
        "因为不知道自己要什么，然后看看别人，他有我没有，就焦虑了。一个知道自己要什么的人，他要的一定是符合自己性情，秉性的，追求这些东西，他才会平静，从容。",
        "人不该太清醒，过去的事情就让它过去，不必反复咀嚼。一生不长，重要的事儿也没那么多。天亮了，又赚了。",
        "",
        "",
        "",
    ]
    msg = msg_list[random.randint(0, len(msg_list) - 1)]
    send_group_msg(msg, group_id)


def tgrj(data):
    """舔狗日记"""
    group_id = str(data["group_id"])
    msg_list = [
        "舔狗日记 3.01 ️ 阴\n她好像从来没有说过爱我，我搜索了一下关键字爱。在我们的聊天记录里，她只说过一次。借我一下爱奇艺会员。",
        "舔狗日记 3.02 多云\n昨天我还是照常给你发了好多消息 今天你终于回了我五个字“烦不烦啊你” 你开始关心我觉不觉得烦了 我太感动了 受宠若惊的 不烦不烦 你天天骂我我都不会觉得你烦",
        "舔狗日记 3.03 雨\n听着窗外稀稀拉拉的雨声 我忽然想到你对我说的话 对啊 生孩子本来就够痛苦了 还管是谁的干嘛呢",
        "舔狗日记 3.04 多云转晴\n现在已经凌晨12点了，我望着手机屏幕迟迟没有她的消息：你知道吗？我等了一晚上你的消息。她终于回复我了：是我让你等的？",
        "舔狗日记 3.05 多云\n她从来不说想我 聊天记录搜索了一下“想你”两个字 全都是:“那波你怎么不上啊 你在想你妈呢”",
        "舔狗日记 3.06 雨\n你回了我一句“傻b” 我翻来覆去思考这是什么意思 sh-a傻 噢你是说我傻 那b就是baby的意思了吧 原来你是在叫我傻宝 这么宠溺的语气 我竟一时不敢相信 其实你也是喜欢我的对吧",
        "舔狗日记 3.07 多云转阴\n你两天没理我了 我发了很多动态都没引起你的注意 我想了很多 可能我是一条鱼在你的海里游 可能我是一颗草 我也愿意被你割 此刻你在干嘛呢 想你",
        "舔狗日记 3.08 晴\n昨天你把我删了，我陷入了久久的沉思，我想这其中一定有什么含义，原来你是在欲擒故纵，嫌我不够爱你，无理取闹的你变得更加可爱了，我会坚守我对你的爱的，你放心好啦！么么哒！今天发工资了 发了1839  给你微信转了520  支付宝1314  还剩下5  傍晚给你发了很多消息你没回 刚弹你正在通话中 你让我别烦 别打扰你跟别人k  好吧没关系宝宝我爱你 所以我不生气 剩下5块我在小卖部买了你爱吃的老坛酸菜牛肉面 给你寄过去了 希望你保护好食欲 我去上班了爱你",
        "舔狗日记 3.09 雨\n我暗恋的人说眼睛疼 所以我买了瓶眼药水寄过去，但她却告诉我她有喜欢的人了 让我别再打扰，距离遥远顺丰都要三天才能到，可她为什么只用了一秒就把眼药水滴进了我眼睛里",
        "舔狗日记 3.10 晴\n今天发工资了，我一个月工资800，你猜我会给你多少，是不是觉得我会给你1200 ，因为厂里全勤奖还有400，错了，我会再和工友借114凑够1314转给你。",
        "舔狗日记 3.11 晴转多云\n你说你情头是一个人用的 空间上锁是因为你不喜欢玩空间 情侣空间是和闺蜜开的 找你连麦时你说你在忙工作 每次聊天你都说在忙 你真是一个上进的好女孩 你真好 我好喜欢你。",
        "舔狗日记 3.12 雨\n每次我发了好几行的文字，你只回复了嗯，哦，啊，好的。我太感动了，无论我说什么你总这样对我百依百顺的，我怎么会有其他的要求呢。尤其每个夜晚，我说晚安，宝贝，总是等不到没有回复的晚安，原来你就这样让我彻夜难眠想你，欲擒故纵这招高明，一直拴住我的心，让我无法摆脱你，我离不开你的。",
        "舔狗日记 3.13 多云转晴\n小时候抓周抓了个方向盘 爸妈都以为我长大了会当赛车手 最差也是个司机 没想到我长大了当了你的备胎",
        "舔狗日记 3.14 雨\n吃过晚餐了，掏出手机，他们都说今天是白色情人节。我点开与你的对话框，发了一句：“在吗？”过了半个小时你也没有回复我，我又发了一条：“不在也行。”\n我委屈，我想你。over",
        "舔狗日记 3.15 雨\n我坐在窗边给你发了99条消息，你终于肯回我了，你说“发你妈啊” 我一下子就哭了，原来努力真的有用，你已经开始考虑想见我的妈妈了，你也是挺喜欢我的。",
        "舔狗日记 3.16 晴\n今天你来上班了，我抢着给你测体温，体温计居然坏了，这让我和你多呆了20秒钟，害得你迟到了，你很生气地走了，一句话都没留下。刚刚微信上给你道歉还给你发了200块钱红包，你很快速地领取了，但迟迟不回我一个字。我想你可能沉浸在感动中吧，我给你发了个句中午吃点好的。回复我的却是一个红色感叹号，红色代表爱情，你一定是不好意思说出口，才用这么温婉的方式表达你对我的爱，我也爱你。",
        "舔狗日记 3.17 多云\n疫情已经持续了一个多月 你发了朋友圈 说想吃火锅 我想着现在外面没法吃火锅 跑去超市给你采购了一些火锅食材还有你最喜欢的海底捞底料 给你发消息说我在你小区门口 给你买了些东西 天气有点冷 我等了半天你都没有出现 也没有回我消息 我想你大概是睡觉呢 点开朋友圈看到你正在和别的男生双排王者 我把东西寄存在门卫 给你留言说我走了 你不爱我没关系 不可以饿着自己。",
        "舔狗日记 3.18 晴\n我爸说再敢网恋就打断我的腿\n幸好不是胳膊\n这样我还能继续和你打字聊天\n就算连胳膊也打断了\n我的心里也会有你位置。",
        "舔狗日记 3.19 阴\n她好像从来没有说过晚安，我搜索了一下关键字。在我们的聊天记录里，她只说过一次。我早晚安排人弄死你",
        "舔狗日记 3.21 阴\n口腔溃疡还没好，今天就不舔了。",
        "舔狗日记 3.22 多云\n她好像从来没有说过晚安，我搜索了一下关键字。在我们的聊天记录里，她只说过一次。我早晚安排人弄死你.。",
        "舔狗日记 3.23 阴\n今天她没有理我，我反复斟酌，嗯，她一定是不想让我和她聊天，免得打字太累。她真的太体贴，太善解人意了。哭，对她的喜欢又多了一分。",
        "舔狗日记 3.24 雨\n今天有点儿发烧，躺在床上，给你发消息，问你怎么不关心我？你反问我是不是有病，有病赶紧吃药。我一下子就被你的温柔打动，原来你还是在乎我的。",
        "舔狗日记 3.25 阴\n今天在微博发现了好好笑的事情，想分享给你，可是当我发给你的时候迎接我的只有一个大大的红色感叹号，对啊，今天是你把我删了的第九十六天呀。真的太真实了吧，我翻看了一下我们的聊天记录，喜欢和爱你都没有给我说过，我知道我不帅还长痘但是我真的喜欢你啊，太心酸了。"
        "舔狗日记 3.26 雨\n今天你终于通过我好友了，打招呼的方式还是那么别致，一个阿玛尼包包的淘宝链接，我从兄弟那边借了3000，很快给你买了，你很开心，给我发了可爱的表情包，还对我说了谢谢，你开心，我也就开心了。",
        "舔狗日记 3.26 小雨\n今天你把我的vx删了，这下我终于解放了！以前我总担心太多消息会打扰你，现在我终于不用顾忌，不管我怎么给你发消息，都不会让你不开心了。等我攒够5201314条我就拿给你看，你一定会震惊得说不出话然后哭着说会爱我一辈子。哈哈",
        "舔狗日记 3.27 雨\n今天有点儿发烧，躺在床上，给你发消息，问你怎么不关心我？你反问我是不是有病，有病赶紧吃药。我一下子就被你的温柔打动，原来你还是在乎我的。",
        "舔狗日记 3.31 雨\n昨晚梦到你把我删了，赶紧起来看看，还好，只是拉黑，原来你还是舍不得删掉我。",
    ]
    msg = msg_list[random.randint(0, len(msg_list) - 1)]
    send_group_msg(msg, group_id)
