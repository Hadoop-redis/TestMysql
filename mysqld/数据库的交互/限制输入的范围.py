#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 限制输入的范围.py
@time: 2020/8/11 16:39
@desc: 
"""


# # 限制输入的数为整数
# while True:
#     print("========================载入数据库操作========================")
#     print("1、进入查询操作")
#     print("2、插入数据！")
#     print("3、修改数据！")
#     print("4、增加数据")
#     print("5、退出程序！")
#
# #     number = input("请输入操作选项:")
# #
# # print(type(number), number)
# if number == 1:
#     print("ok1")
# elif number == 2:
#     print("ok2")
# elif number == 3:
#     print("ok3")
# elif number == 4:
#     print("ok4")
# else:
#     print("退出程序！")
while True:
    s = input("number:")
    if not s.isdigit():
        continue
    s = int(s)
    if 1 <= s <= 5:
        break



while True:
    print("========================载入数据库操作========================")
    print("1、进入查询操作")
    print("2、插入数据！")
    print("3、修改数据！")
    print("4、增加数据")
    print("5、退出程序！")
    number = input("请输入操作选项:")
    try:
        number = int(number)
        if isinstance(number, int):
            break
    except Exception as e:
        print("选项错误，请重新输入!")
        continue
# print(type(number), number)
