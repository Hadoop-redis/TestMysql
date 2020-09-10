#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: look.py
@time: 2020/8/18 17:57
@desc: 程序主框架的执行
"""
from todolist.message import look_change
from todolist.openfile import *


def look():
    while True:
        look_change()
        change = input("请输入需要查看的选项：")
        if change == '1':
            look_open()
        elif change == '2':
            look_finished()
        elif change == '3':
            look_notfinished()
        elif change == '4':
            break
        else:
            print("输入错误，请重新输入!")
            continue
