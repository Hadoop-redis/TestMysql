#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: def加密.py
@time: 2020/8/28 13:51
@desc: def函数方法实现加密
"""
import hashlib


def md5vale(key):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    print(key, " ----> ", input_name.hexdigest())


md5vale("hello")
