import os
import json
import linecache
from settings import PROJECT_DIR
from ywwuyi.cqrequest import send_group_msg


class LTAssignation(object):

    def __init__(self):
        if os.path.exists(PROJECT_DIR + "/tmp/ltassignation.json"):
            print("读取联调分配json")
            with open(PROJECT_DIR + "/tmp/ltassignation.json", mode="r") as f:
                d = json.loads(f.read())
            self.assignation_list = d
            print(d)
        else:
            self.assignation_list = []
        self.use_hl_ip_companys = []
        _count = 0
        for line in open(PROJECT_DIR + "/tmp/ltipinhl.txt"):
            _count += 1
            line = str(line).replace(" ", "").replace("\n", "").replace("\r", "")
            self.use_hl_ip_companys.append(line)
            print("{}:{}".format(str(_count), line))

    def save_assignation(self):
        with open(PROJECT_DIR + "/tmp/ltassignation.json", mode="w") as f:
            f.write(json.dumps(self.assignation_list, ensure_ascii=False))

    def get_password_by_id(self, id):
        password = linecache.getline(PROJECT_DIR + "/tmp/password.log", int(id)*2)
        return password[:-1]

    def get_id(self, data):
        group_id = str(data["group_id"])
        message = str(data["message"])
        message_list = message.split(" ")
        if len(message_list) != 2:
            msg = "指令格式有误，例：联调分配 福州慧林网络科技"
            send_group_msg(msg, group_id)
            return
        else:
            company = message_list[1]
            if company not in self.use_hl_ip_companys:
                msg = "企业：{} 不在<客户使用慧林IP>列表内".format(company)
                send_group_msg(msg, group_id)
                return
            for d in self.assignation_list:
                if company in d["company"]:
                    msg = "已经分配过该企业\n{}  {}  http://222.77.182.242:{}  {}  {}\n".format(
                        str(29000 + int(d["id"])),
                        d["company"],
                        str(29000 + int(d["id"])),
                        "admin",
                        d["password"]
                    )
                    send_group_msg(msg[:-1], group_id)
                    return

            assignation_id = len(self.assignation_list) + 1
            password = self.get_password_by_id(assignation_id)
            msg = "{}\nhttp://222.77.182.242:{}\nadmin\n{}".format(company, str(assignation_id + 29000), password)
            d = {}
            d["id"] = str(assignation_id)
            d["company"] = company
            d["password"] = password
            self.assignation_list.append(d)
            self.save_assignation()
            send_group_msg(msg, group_id)
            return

    def get_info(self, data):
        group_id = str(data["group_id"])
        msg = ""
        count = 0
        if len(self.assignation_list) == 0:
            send_group_msg()
        for i in range(len(self.assignation_list)):
            d = self.assignation_list[i]
            # msg += "{}  {}  {}\n".format(d["id"], str(29000 + int(d["id"])), d["company"])
            msg += "{}  {}  http://222.77.182.242:{}  {}  {}\n".format(
                str(29000 + int(d["id"])),
                d["company"],
                str(29000 + int(d["id"])),
                "admin",
                d["password"]
            )
            count += 1
            if count == 20:
                send_group_msg(msg, group_id)
                msg = ""
                count = 0
        send_group_msg(msg[:-1], group_id)

    def search(self, data):
        group_id = str(data["group_id"])
        message = str(data["message"])
        message_list = message.split(" ")
        if len(message_list) != 2:
            msg = "指令格式有误，例：查询分配 福州慧林"
            send_group_msg(msg, group_id)
            return
        else:
            company = message_list[1]
            msg = ""
            for d in self.assignation_list:
                if company in d["company"]:
                    msg += "{}  {}  http://222.77.182.242:{}  {}  {}\n".format(
                        str(29000 + int(d["id"])),
                        d["company"],
                        str(29000 + int(d["id"])),
                        "admin",
                        d["password"]
                    )
                    send_group_msg(msg[:-1], group_id)
                    return
            msg = "未分配 {}".format(company)
            send_group_msg(msg[:-1], group_id)

    def delete(self, data):
        message = str(data["message"])
        message_list = message.split(" ")
        company = message_list[1]
        for i in range(len(self.assignation_list)):
            d = self.assignation_list[i]
            if d["company"] == company:
                del self.assignation_list[i]
                self.save_assignation()

ltassignation = LTAssignation()
