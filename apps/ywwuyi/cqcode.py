def parse_at(user_id):
    return "[CQ:at,qq={}]".format(str(user_id))


def parse_image(filepath):
    return "[CQ:image,file={}]".format(filepath)