#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: main.py
@time: 2020/8/11 11:06
@desc: 
"""
import pymysql
con = pymysql.connect(host='192.168.11.128', port=3306,
                      user='root', passwd='root')

# 获取游标
cur = con.cursor()
cur.execute("show databases;")
ret = cur.fetchall()
print(ret)

cur.close()
con.close()
