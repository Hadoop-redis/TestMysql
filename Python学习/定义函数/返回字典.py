#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 返回字典.py
@time: 2020/8/14 10:33
@desc: 
"""


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] =age
    return person


musician = build_person('jimi', ' hendrix', age=27)
print(musician)