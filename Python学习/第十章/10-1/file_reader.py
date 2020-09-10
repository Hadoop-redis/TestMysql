#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: file_reader.py
@time: 2020/8/17 10:55
@desc: 打开并读取pi_digits.txt这个文件，再将其内容显示到屏幕上
"""
# file_path = 'D:\\file\\pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)

# 逐行读取
# file_path = 'D:\\file\\pi_digits.txt'
#
# with open(file_path) as file_path:
#     for line in file_path:
#         # rstrip()去掉多余空行
#         print(line.rstrip())

# 创建一个包含文件各行内容的列表
file_path = 'D:\\file\\pi_digits.txt'
with open(file_path) as file_object:
    # 将文件的各行存储在一个列表lines中
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
# 创建一个字符串，它包含文件中存储的所有数字，且没有任何空格
pi_string =''
for line in lines:
    # .strip() 删除空格
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyyyy:")
if birthday in pi_string:
    print("ok!")
else:
    print("no!")
# print(pi_string)
# print(len(pi_string))