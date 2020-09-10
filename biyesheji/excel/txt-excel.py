#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: txt-excel.py
@time: 2020/8/28 11:08
@desc: 将txt文件的数据读取写入到excel文件
"""
import os
import xlwt
import re

# 获取当前目录
a = os.getcwd()

# 定位目录，获取定位之后的目录
os.chdir('D:/file')
a = os.getcwd()

with open(a + '/test.txt') as raw:
    for line in raw:
        print(line.rstrip())
