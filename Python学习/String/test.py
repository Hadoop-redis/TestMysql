#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test.py
@time: 2020/8/10 15:08
@desc: Python中的字符串str用单引号(' ')或双引号(" ")括起来，同时使用反斜杠(\)转义特殊字符。
"""
s = 'Yes,he doesn\'t'
print(s)
print(s, type(s), len(s))

# 如果你不想让反斜杠发生转义，可以在字符串前面添加一个r，表示原始字符串：
print('C:\some\name')

print(r'C:\some\name')