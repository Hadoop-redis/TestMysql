#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 返回值.py
@time: 2020/8/10 17:41
@desc: 
"""


# def return_sum(x, y):
#     c = x + y
#     return c
#
#
# res = return_sum(4, 5)
# print(res)
# 可变参数列表
def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


if __name__ == '__main__':
    ret = arithmetic_mean(19, 41, 12, 123)
    print(ret)
