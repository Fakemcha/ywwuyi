# -*- coding: UTF-8 -*-
import re


if __name__ == '__main__':
    # with open("/home/wxz.html", "r") as f:
    #     content = f.read()
    #
    # links = re.findall(r"(#.*?#)", content)
    # # print(links)\
    # with open("/home/wxz.txt", "a+") as f:
    #     for i in links:
    #         print(i)
    #         try:
    #             print(str(i).encode('utf-8').decode("unicode_escape"))
    #             f.write(str(i).encode('utf-8').decode("unicode_escape") + "\n")
    #         except Exception:
    #             pass
    l = []
    for line in open("/home/wxz.txt"):
        print(line)
        l.append(line.replace("\n", ""))
    import json
    print(l)
    with open("/home/mqmmw/mqmmw/public/static/cqcache/wxz.json", "w") as f:
        f.write(json.dumps(l,ensure_ascii=False))