#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: raw_input.py
@time: 2020/8/10 16:53
@desc: raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
       python3将raw_input和input进行了整合，只有input
"""
# fo = open("foo.txt", "wb")
# fo.close()
# print("文件名：", fo.name)
# print("是否已关闭", fo.closed)
# print("访问模式", fo.mode)
fo = open("foo.txt", "r", encoding='utf8')
s = fo.read()
print(s)