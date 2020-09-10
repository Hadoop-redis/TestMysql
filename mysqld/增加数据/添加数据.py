#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 添加数据.py
@time: 2020/8/7 11:28
@desc: 
"""
import pymysql
conn = pymysql.connect(host="192.168.11.128",
                       user="root",
                       password="root",
                       database="test",
                       charset="utf8")
cursor =conn.cursor()
sql = "INSERT INTO user1(name, age) VALUES (%s, %s);"
username = "Alex"
age = 18

cursor.execute(sql, [username, age])
conn.commit()
cursor.close()
conn.close()