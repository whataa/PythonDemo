# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.lib.cdut.edu.cn/newbook/list.asp?classid=20',
]
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('li', class_='mainlist_li_soft'):
    subItem = item.a.find_next_sibling()
    print('href =', r'http://www.lib.cdut.edu.cn' + str(subItem['href']).strip())
    print('title =', str(subItem['title']).strip())
    print('time =', ''.join(re.findall(r'\d+', str(subItem['title']))))
    # print('time =', str(item.span.em.string).strip())
