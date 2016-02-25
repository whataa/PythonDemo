import json
import re

import requests
from bs4 import BeautifulSoup


class DefaultSpider:
    def __init__(self, url, aid):
        self.__url = url
        self.__aid = aid
        self.__pt = re.compile(r'：(.*)')
        self.__content = []

    def start(self):
        rp = requests.get(self.__url)
        soup = BeautifulSoup(rp.content, 'html.parser')
        # 发布者
        self.__author = re.findall(self.__pt, str(soup.find('span', class_='puber').text).replace('\n', ''))[0]
        # 发布时间
        self.__datetime = re.findall(self.__pt, str(soup.find('span', class_='pubtime').text).replace('\n', ''))[0]
        content = soup.find('div', id='contentdisplay')
        for p in content.find_all('p'):
            # 图片链接
            if p.img:
                self.__content.append({'img': p.img['src']})
            # 是否有内容标签
            elif p.span:
                # 标签里没有内容
                if not p.span.text:
                    continue
                if str(p.text).strip().startswith('附件：'):
                    if p.a:
                        # 可为空
                        self.file_url = p.a['href']
                        self.file_name = str(p.text).strip().replace('\n', '').replace('附件：', '')
                        self.file_type = self.file_url.split('.')[-1]
                    continue
                if p.a:
                    self.__content.append({'href': p.a['href']})
                    continue
                if not str(p.text).strip():
                    continue
                if p.has_attr('align'):
                    self.__content.append({'content': str(p.text).strip().replace('\n', ''), 'align': p['align']})
                    continue
                self.__content.append(
                    {'content': str(p.text).strip().replace('\n', '')})
        self.__content = json.dumps(self.__content, ensure_ascii=False)

        content_id = self.__save(self.__aid)
        if self.__url:
            self.__savefile(content_id)

    def __save(self, aid):
        pass

    def __savefile(self, cid):
        pass
