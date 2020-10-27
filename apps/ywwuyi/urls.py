from django.conf.urls import url
from ywwuyi.views.views import TestJsonView, CommandView, CommandView2, SBPZ
from ywwuyi.views.coolq import SendGroupMsgView, SendPrivateMsgView, DeleteMsgView

urlpatterns = [
    # url(r'test/', TestJsonView.as_view(), name="ywwuyi_test"),
    # url(r'command/', CommandView.as_view(), name="ywwuyi_command"),
    # url(r'command2/', CommandView2.as_view(), name="ywwuyi_command2"),
    # url(r'sbpz/', SBPZ.as_view(), name="SBPZ"),
    url(r'^send_group_msg', SendGroupMsgView.as_view(), name='send_group_msg'),
    url(r'^send_private_msg', SendPrivateMsgView.as_view(), name='send_private_msg'),
    url(r'^delete_msg', DeleteMsgView.as_view(), name='delete_msg'),
    url(r'^ban', DeleteMsgView.as_view(), name='ban'),
]