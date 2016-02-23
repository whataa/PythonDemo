# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re
import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.lib.cdut.edu.cn/libnews/html/821.html',
    r'http://www.lib.cdut.edu.cn/libtrain/html/810.html',
    r'http://www.lib.cdut.edu.cn/libtrain/html/808.html',
    r'http://www.lib.cdut.edu.cn/libnews/html/815.html',
]

rp = requests.get(url[2])
soup = BeautifulSoup(rp.content, 'html.parser')
#内容
content = soup.find('div', id='passage')
first_tr = content.table.find('tr')
print(first_tr.text)
for next in first_tr.find_next_siblings():
    #删除分享
    if next.find(class_='bshare-custom'):
        del next
        continue
    print(next)
# for tr in content.table.find_all('tr'):
#     # if tr.find('table'):
#     #     print(tr)
#     #     continue
#     if not tr.td.div:
#         print(tr.td.text)
#         continue
#     for div in tr.td.find_all('div'):
#         #忽略“分享”
#         if div.get('class'):
#             continue
#         if div.text and (not str(div.text).strip()):
#             continue
#         print(str(div.text).strip().replace('\n',''))