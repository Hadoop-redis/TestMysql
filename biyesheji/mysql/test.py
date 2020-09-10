#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test.py
@time: 2020/8/13 10:07
@desc: 
"""
import pymysql

# def fun(n):
#     sum = 0
#     for i in range(n + 1):
#         sum += i
#     return sum
#
#
# print(fun(10))
import pymysql


# 连接模块
def connection():
    global conn, cursor
    conn = pymysql.connect(host="192.168.11.128",
                           user="root",
                           password="root",
                           database="Linux",
                           charset="utf8")
    cursor = conn.cursor()
    # return conn


# 增加数据
def add():
    global add_sql
    add_sql = "insert into network values('Linux2', 'NAT连接', 1, 2);"


# 删除数据
def delete():
    global delete_sql
    delete_sql = "delete from information where ip='192.168.11.15';"


# 修改数据
def update():
    global update_sql
    update_sql = "update network set kernel_amout=2 where name='Linux1';"


# 查询模块
def select(table):
    global sql
    sql = "select * from " + table + ";"
    # return sql


# 关闭模块
def close():
    cursor.close()
    conn.close()


connection()
table = input("请输入表名：")
select(table)
cursor.execute(sql)
rets = cursor.fetchall()
for ret in rets:
    print(ret)
close()
