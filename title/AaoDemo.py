# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.aao.cdut.edu.cn/aao/aao.php?sort=389&sorid=391&from=more',
]
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('img', alt='news'):
    subItem = item.find_next_sibling()
    # print(subItem)
    print('href =', r'http://www.aao.cdut.edu.cn' + str(subItem['href']).strip())
    print('title =', str(subItem['title']).strip())
    print('time =', str(subItem.span.string).strip().replace('(', '').replace(')', ''))
