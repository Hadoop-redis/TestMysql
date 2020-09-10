#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: write.py
@time: 2020/8/17 13:56
@desc: r:读取模式  w:写入模式（写入前会清空之前的内容）  a:附加模式  r+:读取和写入
       省略不写时，默认为只读模式打开文件。
       Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，
       必须先使用函数str()将其转换为字符串格式。
"""
filename = 'programming.txt'

# 如果写入的文件不存在，函数open()会自动创建它
with open(filename, 'w') as file_object:
    file_object.write("I love you,think it maybe!\n")
    # 写入多行时，write()不会在文本末尾添加换行符，所以要指定换行符.
    file_object.write("Hello Python!\n")
    file_object.write("Hello World!")