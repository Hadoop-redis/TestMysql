#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: message.py
@time: 2020/8/18 17:10
@desc: 显示功能菜单
"""
import time

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def message():
    print("======================todoList======================")
    print("1、查看事项.")
    print("2、新加待办事项.")
    print("3、标记待办事项的完成状态")
    print("4、退出程序！")


def look_change():
    print("=========================请输入需要查看的内容=========================")
    print("1、查看所有事项.")
    print("2、查看已经完成事项.")
    print("3、查看未完成事项.")
    print("4、返回上一级.")
