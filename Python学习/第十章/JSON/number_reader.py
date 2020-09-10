#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: number_reader.py
@time: 2020/8/17 14:49
@desc: 
"""
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    # 使用json.load()将这个列表读取到内存中
    numbers = json.load(f_obj)

print(numbers)