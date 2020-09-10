#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 返回简单值.py
@time: 2020/8/14 10:25
@desc: 
"""


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    # return full_name.format()
    # .title() 将full_name的值转换为首字母大写格式
    return full_name.title()


musician = get_formatted_name('Jimi', 'Hendrix')
print(musician)
