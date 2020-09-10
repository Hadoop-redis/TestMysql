#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 返回字典格式数据.py
@time: 2020/8/7 11:23
@desc: 
"""
import pymysql

conn = pymysql.connect(host="192.168.11.128",
                       user="root",
                       password="root",
                       database="test",
                       charset="utf8")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = """
CREATE TABLE USER2 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
cursor.close()
conn.close()