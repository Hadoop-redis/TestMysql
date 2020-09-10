#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test1.py
@time: 2020/8/28 13:47
@desc: 通过argv实现加密
    在Terminal中改目录下运行：python test1.py 需要加密的字符
"""
import hashlib
import sys
from sys import argv

# 要加密的字符串
input_name = hashlib.md5()
# 获取要加密的字符串
argv1 = sys.argv[1]
input_name.update(argv1.encode("utf-8"))
print(input_name.hexdigest())
