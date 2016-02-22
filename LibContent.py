# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re
import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.lib.cdut.edu.cn/libnews/html/821.html',
    r'http://www.lib.cdut.edu.cn/libtrain/html/810.html',
    r'http://www.lib.cdut.edu.cn/libtrain/html/808.html',
]

rp = requests.get(url[2])
soup = BeautifulSoup(rp.content, 'html.parser')
#内容
content = soup.find('div', id='passage')
for tr in content.table.find_all('tr'):
    if not tr.td.div:
        print(tr.td.text)
    for div in tr.td.find_all('div'):
        if div.get('style'):
            print(str(div.text).strip().replace('\n',''))