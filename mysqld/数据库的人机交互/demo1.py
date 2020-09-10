#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: demo1.py
@time: 2020/8/7 11:40
@desc: 写函数：创建库、创建表、增加数据、删除数据、修改数据、查询数据
添加功能：读取本地文件写入数据库、将数据库的数据下载到本地并保存
"""
import pymysql

host = input("请输入连接地址：")
user = input("请输入用户名：")
password = input("请输入用户密码：")
# dbname = input("请输入数据库名称：")
conn = pymysql.connect(host=host, port=3306,
                       user=user, password=password,)
                       # db=dbname)
cursor = conn.cursor()
# sql = "select * from books;"
sql = "show databases;"
cursor.execute(sql)
ret = cursor.fetchall()
cursor.close()
# 关闭数据库连接
conn.close()
# 遍历数据
for i in ret:
    print(i)

