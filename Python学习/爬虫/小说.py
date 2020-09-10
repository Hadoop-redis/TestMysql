#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 小说.py
@time: 2020/8/16 21:20
@desc: 
"""
import re
import requests
from bs4 import BeautifulSoup
from tqdm import trange
import time

# 头部伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36 QIHU 360SE '
}

url = "https://www.rzlib.net/b/63/63037/46523518.html"
req = requests.get(url, headers=headers)
req.encoding = 'utf8'
html = req.text
data = BeautifulSoup(html, " html.parser")

req.encoding = 'utf8'

section_name = data.title.string
print(section_name)
