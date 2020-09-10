#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: demo1.py
@time: 2020/8/10 17:31
@desc: 
"""


# def hello():
#     print("Hello World!")
#
#
# hello()
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))