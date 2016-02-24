# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.gra.cdut.edu.cn/plus/list.php?tid=14',
]
pattern = re.compile(r'</small>(.*) <small>')
rp = requests.get(url[0])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all(class_='title'):
    print('href =', r'http://www.gra.cdut.edu.cn' + str(item['href']).strip())
    print('title =', str(item.string).strip())
    print('time =', re.search(pattern, str(item.find_next_sibling()))
          .group().replace('</small>','').replace('<small>',''))