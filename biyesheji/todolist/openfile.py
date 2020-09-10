#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: openfile.py
@time: 2020/8/19 9:02
@desc: 
"""
from todolist.message import date

filename = "D:\\file\\test.txt"


# 查看所有的待办事项
def look_open():
    print("=================所有事项=================")
    with open(filename) as f_obj:
        for i in f_obj.readlines():
            print(i.rstrip())


# 查看已经完成的事项
def look_finished():
    print("=================已经完成的=================")
    with open(filename) as f_obj:
        for i in f_obj.readlines():
            res = i.split('\t')[3].rstrip()
            if res == 'T':
                print(i.rstrip())


# 查看为完成的待办事项
def look_notfinished():
    print("=================未完成的待办事项=================")
    with open(filename) as f_obj:
        for i in f_obj.readlines():
            res = i.split('\t')[3].rstrip()
            if res == 'F':
                print(i.rstrip())


# 新增待办事项
def look_add():
    with open(filename) as f:
        for i in f.readlines():
            res = i.split('\t')[0].rstrip()
        # print(int(res) + 1),
        number = int(res) + 1
    with open(filename, 'a') as f_obj:
        res = input("请添加待办事项：")
        f_obj.write(str(number) + "\t" + date + "\t" + res + "\tF\n")


# 修改待办事项状态
def look_alter():
    while True:
        print("====================修改待办事项状态====================")
        with open(filename) as f_obj:
            for i in f_obj.readlines():
                print(i.rstrip())
        with open(filename, 'r') as f_obj:
            lines = f_obj.readlines()
            number = int(input("请输入需要修改的行号："))
            fields = lines[number - 1].split('\t')
            status = input("请输入需要修改的完成状态：\nF：表示未完成\nT：表示已经完成\nq:返回上一级\n:")
        if status == 'T':
            fields[-1] = status + '\n'
            # 把修改好的元素列表合并成一行
            lines[number - 1] = '\t'.join(fields)
            # 把所有行写回文件
            open(filename, 'w').writelines(lines)
        elif status == 'F':
            fields[-1] = status + '\n'
            lines[number - 1] = '\t'.join(fields)
            open(filename, 'w').writelines(lines)
        elif status == 'q':
            break
        else:
            print("输入错误，请重新输入!")
            continue
