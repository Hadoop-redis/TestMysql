#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 基本使用建表.py
@time: 2020/8/7 11:19
@desc: 
"""
import pymysql
conn = pymysql.connect(host="192.168.11.128",
                       user="root",
                       password="root",
                       database="test",
                       charset="utf8mb4")
cursor = conn.cursor()
sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
cursor.close()
conn.close()