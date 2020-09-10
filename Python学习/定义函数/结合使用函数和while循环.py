#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 结合使用函数和while循环.py
@time: 2020/8/14 10:38
@desc: 
"""


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


# 这是一个无限循环，while循环让用户输入姓名.
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First_name:")
#     l_name = input("Last_name:")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + " !")


# 定义退出循环
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First_name:")
    if f_name == 'q':
        break

    l_name = input("Last_name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")