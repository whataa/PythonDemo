# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码

import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.cdut.edu.cn/xww/news2_tzgg.html',
    r'http://www.cdut.edu.cn/xww/news2_xs.html',
    r'http://www.cdut.edu.cn/xww/news2_zl.html',
    r'http://www.cdut.edu.cn/xww/news2_yw.html',
]
rp = requests.get(url[3])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('li'):
    print('href =', str(item.a['href']).strip())
    print('title =', str(item.a['title']).strip())
    print('time =', str(item.span.string).strip().replace('\n', ''))
