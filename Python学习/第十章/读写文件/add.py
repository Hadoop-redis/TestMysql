#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: add.py
@time: 2020/8/17 14:10
@desc: 添加内容到文本中
"""
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also finding meaning in large datasets.\n")
    file_object.write("I think english is very bad!\n")