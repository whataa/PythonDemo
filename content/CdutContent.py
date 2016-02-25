# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import json

import re
import requests
from bs4 import BeautifulSoup

url = [
    # 公告&学术
    r'http://www.cdut.edu.cn/xww/news/145154845001077854.html',
    r'http://www.cdut.edu.cn/xww/news/145489653138558663.html',
    r'http://www.cdut.edu.cn/xww/news/145621441566681942.html',
    r'http://www.cdut.edu.cn/xww/news/145085388618242647.html',
    # 要闻&媒体
    r'http://www.cdut.edu.cn/xww/news/145310363911994028.html',
    r'http://www.cdut.edu.cn/xww/newPage.do?xwbh=145352399438538578&yyxwym=news',
    # 专栏
    r'http://www.cdut.edu.cn/xww/news/145198579690096955.html'
]
pt = re.compile(r'：(.*)')
rp = requests.get(url[1])
soup = BeautifulSoup(rp.content, 'html.parser')

# 发布者
__author = re.findall(pt,str(soup.find('span', class_='puber').text).replace('\n', ''))[0]
# 发布时间
__datetime = re.findall(pt,str(soup.find('span', class_='pubtime').text).replace('\n', ''))[0]

__content = []
file_url = ''
file_name = ''
file_type = ''
for p in soup.find_all('p', class_='MsoNormal'):
    # 图片链接
    if p.img:
        __content.append({'img': p.img['src']})
    # 是否有内容标签
    elif p.find('span'):
        # 标签里没有内容
        if not p.span.text:
            continue
        if str(p.text).strip().startswith('附件：') or str(p.text).strip().startswith('下载：'):
            if p.a:
                file_url = p.a['href']
                file_name = str(p.text).strip().replace('\n', '').replace('附件：', '').replace('下载：','')
                file_type = file_url.split('.')[-1]
            continue
        if p.a:
            __content.append({'href': p.a['href']})
            continue
        if not str(p.text).strip():
            continue
        if p.has_attr('align'):
            __content.append({'content': str(p.text).strip().replace('\n', ''), 'align': p['align']})
            continue
        __content.append({'content': str(p.text).strip().replace('\n', '')})

print(__author)
print(__datetime)
print(json.dumps(__content,ensure_ascii=False))
if file_name:
    print(file_name)
    print(file_url)
    print(file_type)
