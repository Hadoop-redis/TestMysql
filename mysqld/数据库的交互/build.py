#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: build.py
@time: 2020/8/11 10:37
@desc: 新建数据库
"""
import pymysql
print("==================载入mytsql数据库==================")
con = pymysql.connect(host='192.168.11.128', user='root',
                      passwd='root', charset='utf8')
print('连接成功')
# 获取游标
cur = con.cursor()
cur.execute("create database test_db")
print('创建test_db库完成')
cur.execute('use test_db;')
print('进入test_db库完成')
cur.execute("create table test_db(id int, name char(20))")
print('创建表完成')

cur.close()
print('游标关闭完成')
con.close()
print('关闭连接')
print("=====================程序结束=====================")