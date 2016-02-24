# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.lib.cdut.edu.cn',
]
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('li', class_='mainlist_li_notice'):
    print('href =', r'http://www.lib.cdut.edu.cn' + str(item.a['href']).strip())
    print('title =', str(item.a['title']).strip())
    print('time =', str(item.span.em.string))
    # print('time =', str(item.span.em.string).strip())
