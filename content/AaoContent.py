# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码
import re
import requests
from bs4 import BeautifulSoup

url = [
    r'http://www.aao.cdut.edu.cn/aao/aao.php?aid=12395&sort=389&sorid=391&from=passg',
    r'http://www.aao.cdut.edu.cn/aao/aao.php?aid=12394&sort=389&sorid=391&from=passg',
    r'http://www.aao.cdut.edu.cn/aao/aao.php?aid=1236&sort=389&sorid=391&from=passg',
    r'http://www.aao.cdut.edu.cn/aao/aao.php?aid=1231&sort=389&sorid=391&from=passg',
]
pt = re.compile(r'/> (.*) <a')

rp = requests.get(url[3])
soup = BeautifulSoup(rp.content, 'html.parser')
#内容
content = soup.find('div', id='text')
for p in content.p.find_all('p'):
    if not p.text:
        continue
    if not str(p.text).strip():
        continue
    print(str(p.text).strip().replace('\n',''))
#表格
if content.p.find('table'):
    print(str(content.p.table))
#附件
if content.p.find('a'):
    print(re.findall(pt, str(content.p))[0])
    #移除链接前的.符号
    print(r'http://www.aao.cdut.edu.cn/aao' + content.p.a['href'][1:])