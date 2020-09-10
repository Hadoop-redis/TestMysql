#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: number_writer.py
@time: 2020/8/17 14:42
@desc: 演示如何使用json.dump()来存储数字列表
"""
import json

numbers = [2, 3, 5, 7, 11, 13]

# 指定了要将该数字列表存储到其中的文件的名称
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    # 使用函数json.dump()将数字列表存储到文件numbers.json中
    json.dump(numbers, f_obj)