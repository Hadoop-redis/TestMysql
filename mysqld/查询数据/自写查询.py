#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 自写查询.py
@time: 2020/8/7 10:57
@desc: 
"""
# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="192.168.11.128",
                       user="root",
                       password="root",
                       database="test1",
                       charset="utf8mb4")
# 得到一个可以执行的 SQL语句
cursor = conn.cursor()
# 查询数据的SQL语句
sql = "select * from books;"
# 执行SQL语句
cursor.execute(sql)
"""
获取数据
获取多条数据：cursor.fetchall()
获取单条数据：cursor.fetchone()
"""
# 获取数据
ret = cursor.fetchall()
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
# 遍历数据
for i in ret:
    print(i)
