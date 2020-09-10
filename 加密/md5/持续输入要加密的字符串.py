#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 持续输入要加密的字符串.py
@time: 2020/8/28 13:56
@desc: 持续输入要加密的字符串
"""
# 导入加密算法
import hashlib
count = 0
loop = 0

while count == 0:
    key = input("请输入要加密的md5：")
    # 初始化加密模板
    input_name = hashlib.md5()
    # 添加要加密的字节
    input_name.update(key.encode("utf-8"))
    # 进行加密
    m = input_name.hexdigest()
    loop += 1
    print("第", loop, "次:\n", key, " ----> ", m)
    print("-" * 30)

