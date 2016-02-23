# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re
import requests
from bs4 import BeautifulSoup

url = [
    #公告&学术
    r'http://www.cdut.edu.cn/xww/news/145154845001077854.html',
    r'http://www.cdut.edu.cn/xww/news/145489653138558663.html',
    #要闻&媒体
    r'http://www.cdut.edu.cn/xww/news/145310363911994028.html',
    r'http://www.cdut.edu.cn/xww/newPage.do?xwbh=145352399438538578&yyxwym=news',
    #专栏
    r'http://www.cdut.edu.cn/xww/news/145198579690096955.html'
]

rp = requests.get(url[2])
soup = BeautifulSoup(rp.content, 'html.parser')
#发布者
puber = soup.find('span', class_='puber')
print(str(puber.text).replace('\n',''))
#发布时间
pubtime = soup.find('span', class_='pubtime')
print(str(pubtime.text).replace('\n',''))

content = soup.find('div', id='contentdisplay')
for p in content.find_all('p'):
    #图片链接
    if p.img:
        print(p.img['src'])
    #是否有内容标签
    elif p.span:
        #标签里没有内容
        if not p.span.text:
            continue
        print(str(p.text).strip().replace('\n',''))
        if p.a:
            print(p.a['href'])

