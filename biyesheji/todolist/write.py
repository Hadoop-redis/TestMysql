#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: write.py
@time: 2020/8/18 10:30
@desc: 记录用户的今日待办事项保存在磁盘文件中,并在需要时可以将所有待办事项打印出来
       并可标记待办事项的完成状态，此程序至少由两个模块组成。
"""
from todolist.message import *
from todolist.look import *


def run_test():
    while True:
        message()
        res = input("请输入选项：")
        if res == '1':
            look()

        elif res == '2':
            look_add()

        elif res == '3':
            look_alter()

        elif res == '4':
            print("退出程序！！！")
            break

        else:
            print("输入错误，请重新输入！")
            continue
