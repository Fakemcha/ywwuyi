from ywwuyi.qqproxy.sendmessage import SendQQMessage

def magnet(qqmessage):
    group_id = qqmessage.get_group_id()
    message = qqmessage.get_content()
    sqm = SendQQMessage()
    sqm.add_group_id(group_id)
    sqm.add_content("magnet:?xt=urn:btih:" + message)
    sqm.send()