# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.cist.cdut.edu.cn/plus/list.php?tid=25',
]
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('span'):
    if item.a:
        continue
    if not item.find_next_sibling():
        continue
    sibItem = item.find_next_sibling()
    print('href =', r'http://www.cist.cdut.edu.cn' + str(sibItem['href']).strip())
    print('title =', str(sibItem.string).strip())
    print('time =', str(item.string).replace(' ', ''))
