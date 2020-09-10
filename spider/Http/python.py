#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: python.py
@time: 2020/8/19 14:52
@desc: 
"""
import urllib.request

response = urllib.request.urlopen('https://www.baidu.com')
print(response.read().decode('utf8'))