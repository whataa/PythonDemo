import re

import requests
from bs4 import BeautifulSoup
from django.db import models


class Article(models.Model):
    pass

class CdutSpider:
    def __init__(self, url):
        self._url = url
        self.href = []
        self.title = []
        self.datetime = []
        self.aid = []
    def start(self):
        pattern = re.compile(r'news/(.{10})')
        rp = requests.get(self._url)
        soup = BeautifulSoup(rp.content, 'html.parser')
        for item in soup.find_all('li'):
            self.aid.append(Article().save())
            self.href.append(str(item.a['href']).strip())
            self.title.append(str(item.a['title']).strip())
            self.datetime.append(re.findall(pattern, str(item.a['href']))[0])