import json
import time
from bs4 import BeautifulSoup

from independent_init import django_init

django_init()
from ywwuyi.config import headers
from ywwuyi.models.lyric import Lyric

from apps.common.request import request_by_url

# def request_by_url(url):
#     print(url)
#     time.sleep(3)
#     if "https://" in url:
#         ssl._create_default_https_context = ssl._create_unverified_context
#     request = urllib.request.Request(urllib.parse.quote(url, safe=string.printable), headers=headers)
#     resopen = urllib.request.urlopen(request, timeout=10)
#     response = resopen.read()
#     # print (response)
#     return response

def parseHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul_tag = soup.ul
    div_tag = ul_tag.find_all('div',class_='name')
    index = 0
    for i_a in div_tag:
        a_tag = i_a.find('a')
        music_name = a_tag.string         #歌名
        music_url = a_tag.get('href')  #歌名对应的url 
        print(music_name, music_url)
        if '(' in music_name and ')' in music_name and '(with' not in music_name:
            continue
        if '伴奏' in music_name or '铃声' in music_name or 'Live' in music_name:
            continue
        else:
            lrc_url = 'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={}'.format(str(music_url).replace('/yinyue/', ''))
            print (lrc_url)
            lrc_html = ""
            lrc_dict = {}
            while not lrc_html:
                lrc_html = str(request_by_url(lrc_url, sleep=7), encoding='utf-8')
                lrc_dict = json.loads(lrc_html)
            # print(lrc_html)
            if not lrc_dict['data']['lrclist']:
                continue

            lrc_dict = json.loads(lrc_html)
            lrc = ""
            for lrc_item in lrc_dict['data']['lrclist']:
                # print(lrc_item['lineLyric'])
                lrc += (lrc_item['lineLyric'] + '\n')
            print(lrc[:-1])
            if '纯音乐请欣赏' not in lrc[:-1]:
                lyric = Lyric.objects.filter(title=music_name).first()
                if not lyric:
                    Lyric.objects.create(
                        title=music_name,
                        singer='许嵩',
                        lyric=lrc[:-1],
                        url=lrc_url
                    )
        
            print('-------------------------------------------------------------')

            index+=1
            # if index==5:
            #     break

def main():
    for i in range(45):
        url = 'http://www.kuwo.cn/artist/contentMusicsAjax?artistId=1887&pn={}&rn=30'.format(i)
        # print (request_by_url(url))
        html = str(request_by_url(url, sleep=3), encoding='utf-8')
        parseHTML(html)

main()

#artistId=歌手ID
#周杰伦 336
#aimer 22690