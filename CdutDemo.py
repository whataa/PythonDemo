# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import requests
from bs4 import BeautifulSoup

url = r'http://www.cdut.edu.cn/xww/news2_tzgg.html'
rp = requests.get(url)
rp.encoding = 'GBK'
# print(rp.text)
soup = BeautifulSoup(rp.content, 'html.parser')
# print(soup.text)
for item in soup.find_all('li'):
    print('href =', item.a['href'])
    print('title =', item.a['title'])
    print('time =', item.span.string.strip('\n'))