# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.zs.cdut.edu.cn/plus/list.php?tid=2',
]
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
item = soup.find_all(class_='right_content')[0]
for subItem in item.find_all('li'):
    # print(subItem)
    print('href =', r'http://www.zs.cdut.edu.cn' + str(subItem.a['href']).strip())
    print('title =', str(subItem.a.string).strip())
    print('time =', str(subItem.span.string))
