#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test.py
@time: 2020/8/17 14:15
@desc: 
"""
while True:
    names = input("请输入用户姓名：")
    if names == 'q':
        break
    else:
        filename = 'name.txt'

        with open(filename, 'a') as file_object:
            file_object.write(names + "\n")
            print("hello " + names + "!")