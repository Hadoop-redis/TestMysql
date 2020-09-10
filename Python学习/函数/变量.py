#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 变量.py
@time: 2020/8/10 17:37
@desc: 
"""
a = 4  # 全局变量


def func1():
    a = 17  # 局部变量
    print("in print_func a = ", a)


def func2():
    print("in print_func a = ", a)


func1()
func2()
print("a = ", a)