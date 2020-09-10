#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 查询库.py
@time: 2020/8/11 9:23
@desc: 
"""
import pymysql
import sys

# host = input("请输入连接地址：")
# user = input("请输入用户名：")
# password = input("请输入用户密码：")
# # dbname = input("请输入数据库名称：")
conn = pymysql.connect(host="192.168.11.128", port=3306,
                       user="root", password="root", )
# 查询有哪些数据库
cursor = conn.cursor()
sql = "show databases;"
cursor.execute(sql)
ret = cursor.fetchall()
print(ret)

# 选择操作是原有数据库还是新建数据库


# dbname = input("请输入库名：")
# conn1 = pymysql.connect(host="192.168.11.128", port=3306,
#                         user="root", password="root",
#                         db=dbname)
# cur = conn1.cursor()
# sql2 = "show tables;"
# cur.execute(sql2)
# ret2 = cur.fetchall()
# print(ret2)


# 关闭游标
cursor.close()
# 关闭数据库连接
conn.close()

