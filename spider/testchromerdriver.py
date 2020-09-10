#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: testchromerdriver.py
@time: 2020/8/19 14:23
@desc: 
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello<p>', 'lxml')
print(soup.text)