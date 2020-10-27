from channels.generic.websocket import WebsocketConsumer
import json, time
from common.logs import write_test_log
from ywwuyi.command.handler import commandHandler
from ywwuyi.models.qq_message import QQMessage
from django.db.models import Count


class CoolQAPIConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data = json.loads(text_data)
        print(text_data)
        write_test_log("----------" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "----------", filename="cq_api.log")
        write_test_log(text_data, filename="cq_api.log")

        message = text_data['message']

        commandHandler.handle(text_data)

        # write_test_log("不等待")
        if text_data["message_type"] == "group":
            if "sender" in text_data and "user_id" in text_data["sender"]:
                qm = QQMessage(
                    subject=text_data["group_id"],
                    user_id=text_data["sender"]["user_id"],
                    content=text_data["message"],
                    type="group",
                    timestamp=text_data["time"]
                )
                qm.save()

        # result = QQMessage.objects.filter(subject='532799508').values('user_id').annotate(Count=Count('user_id')).order_by('-Count')[0]
        # result = QQMessage.objects.filter(subject='532799508')
        # print("result:")
        # print(result)
        # for r in result:
        #     print(r["Count"])
        jd = json.dumps({
            "reply": "cont"
        })

        self.send(text_data=jd)


class CoolQEventConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        write_test_log("----------" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "----------", filename="cq_api.log")
        write_test_log(text_data_json, filename="cq_event.log")

        self.send(text_data=json.dumps({
            'message': ''
        }))