#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: query.py
@time: 2020/8/11 10:41
@desc: 查询数据  https://www.cnblogs.com/desireyang/p/12072899.html
"""
import pymysql

# 1、打开数据库来连接
conn = pymysql.connect(host='192.168.11.128', user='root',
                       password='root', port=3306,
                       database='test', charset='utf8')

# 2、创建游标
cursor = conn.cursor()

# 3、操作数据库
# 如果数据表已经存在使用excute() 方法删除表
cursor.execute("drop table if exists employee")

# 创建数据表SQL语句
sql = """create table employee(
         first_name char(20) not null,
         last_name char(20),
         age int 
         sex char(1)
         income float)"""
cursor.execute(sql)

# 查询数据
sql = "select * from employee where income > {}".format(1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname={},lname={},age={},sex={},income={}".format(fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 3、添加数据
# SQL插入语句
sql = """insert into employee(first_name,
         last_name, age, sex, income)
         values ('Mac', 'Mohan', 10, 'M', 2000)"""
try:
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

# 5、删除数据
# SQL删除语句
sql = "delete from employee where age > {}".format(20)
try:
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

# 4、关闭游标，数据库连接
cursor.close()
conn.close()
