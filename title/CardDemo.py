# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.campuscard.cdut.edu.cn/NewCmsM1/_Notice/noticeList.html',
]
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('tr', class_='odd views-row-first'):
    subItem = item.td
    # print(subItem)
    print('href =', r'http://www.campuscard.cdut.edu.cn' + str(subItem.a['href']).strip())
    print('title =', str(subItem.a.text).strip())
    print('time =', str(subItem.find_next_sibling().text).strip())
