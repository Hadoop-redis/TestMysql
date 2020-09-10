#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 传递列表.py
@time: 2020/8/14 10:52
@desc: 
"""


# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
#
# usernames = ['hannah', ' ty', 'margot']
# greet_users(usernames)


# 传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperson')
make_pizza('mushrooms', 'green peppers', 'extra cheese')