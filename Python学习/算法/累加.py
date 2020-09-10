#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 累加.py
@time: 2020/8/14 9:06
@desc: 
"""


# 第一种算法，运算速度慢于第二种，特别是在运行大量运算时
def func(n):
    thesum = 0
    for i in range(n + 1):
        thesum += i
    return thesum


print(func(100))


# 第二种算法，比第一种运算速度快
def fun(n):
    for x in range(n + 1):
        sum = ((1 + x) * x) / 2
    return sum


print(fun(10))