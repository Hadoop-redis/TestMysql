#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: demo2.py
@time: 2020/8/7 13:38
@desc: 写函数：创建库、创建表、增加数据、删除数据、修改数据、查询数据
添加功能：读取本地文件写入数据库、将数据库的数据下载到本地并保存
"""
import pymysql


# 告诉编译器这是全局变量conn
global conn


def connect_mysql():
    host = input("请输入连接地址：")
    user = input("请输入用户名：")
    password = input("请输入用户密码：")
    dbname = input("请输入数据库名称：")
    conn = pymysql.connect(host=host, port=3306,
                           user=user, password=password,
                           db=dbname)


def sql():
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
    cursor.close()
    # 关闭数据库连接
    conn.close()