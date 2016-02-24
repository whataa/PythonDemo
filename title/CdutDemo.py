# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re
import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.cdut.edu.cn/xww/news2_tzgg.html',
    r'http://www.cdut.edu.cn/xww/news2_xs.html',
    r'http://www.cdut.edu.cn/xww/news2_zl.html',
    r'http://www.cdut.edu.cn/xww/news2_yw.html',
]
#截取链接的时间戳
pattern = re.compile(r'news/(.{10})')
rp = requests.get(url[2])
soup = BeautifulSoup(rp.content, 'html.parser')
for item in soup.find_all('li'):
    print('href =', str(item.a['href']).strip())
    print('title =', str(item.a['title']).strip())
    print('current',re.findall(pattern, str(item.a['href']))[0])
    # print('time =', str(item.find('span', class_='time').text).strip().replace('\n', ''))