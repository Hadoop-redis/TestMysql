#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: def加密.py
@time: 2020/8/11 15:15
@desc: 
"""
import pymysql

# 连接数据库
conn = pymysql.connect(host="192.168.11.128",
                       user="root",
                       password="root",
                       database="test1",
                       charset="utf8")
cursor = conn.cursor()

# 功能菜单
print("========================载入数据库操作========================")
print("1、进入查询操作")
print("2、插入数据！")
print("3、修改数据！")
print("4、增加数据")
print("5、退出程序！")


def connnection_close():
    cursor.close()
    conn.close()

# 限制输入的选项
while True:
    number = input("请输入操作选项:")
    if not number.isdigit():
        print("error")
        continue
    number = int(number)
    if 1 <= number <= 5:
        break
# 查询操作
if number == 1:
    print("==================表列表==================")
    cursor.execute("show tables")
    # x = cursor.fetchall()
    # for i in x:
    #     print(i)
    print(cursor.fetchall())
    table = input("请输入要查询的表：")
    sql = "select * from " + table + ";"
    cursor.execute(sql)
    ret = cursor.fetchall()
    print(ret)
    # for i in ret:
    #     print(i)

    connnection_close()

# 插入操作
elif number == 2:
    print("==================表列表==================")
    cursor.execute("show tables")
    # x = cursor.fetchall()
    # for i in x:
    #     print(i)
    print(cursor.fetchall())
    table = input("请输入要插入数据的表：")
    # print("==================表结构==================")
    # cursor.execute("desc " + table + ";")
    # ret1 = cursor.fetchall()
    # for a in ret1:
    #     print(a)
    if table == "books":
        print("===========================需要插入的字段和类型=========================== \n"
              "数号：book_id(int(6)),           类型号：type_id(varchar(3)) \n"
              "书名：book_name(varchar(50)),    作者：author(varchar(50)) \n"
              "出版社：publisher(varchar(50)),   价格：price(int(3))")
        sql = "INSERT INTO books VALUES(%s, %s, %s, %s, %s, %s);"
        book_id = input("请输入书号--int(6):")
        type_id = input("请输入类型号--varchar(50):")
        book_name = input("请输入书名--varchar(50):")
        author = input("请输入作者--varchar(50):")
        publisher = input("请输入出版社--varchar(50):")
        price = input("请输入书的价格--int(3):")
        cursor.execute(sql, [book_id, type_id, book_name, author, publisher, price])
        conn.commit()
        connnection_close()

    elif table == "borrow_info":
        print("===========================需要插入的字段和类型=========================== \n"
              "读者编号--int(7)：reader_id,           书号--int(6)：book_id \n"
              "时间--date(2005-09-16)：borrow_time,   注释--varchar(200)null：notes")
        sql = "INSERT INTO borrow_info VALUES(%s, %s, %s, %s);"
        reader_id = input("请输入读者编号：")
        book_id = input("请输入书号：")
        borrow_time = input("请输入借阅时间：")
        notes = input("请输入注释：")
        cursor.execute(sql, [reader_id, book_id, borrow_time, notes])
        conn.commit()
        connnection_close()
    elif table == "readers":
        print("===========================需要插入的字段和类型=========================== \n"
              "读者编号--int(7)：reader_id,  读者姓名--varchar(8)：name \n"
              "读者性别--varchar(2)：sex,    读者院系--varchar(16)：dept \n"
              "读者职业--varchar(8)：status, 读者所在学校--varchar(30)：address\n "
              )
        sql = "INSERT INTO readers VALUES(%s, %s, %s, %s, %s, %s);"
        reader_id = input("请输入读者编号：")
        name = input("请输入读者姓名：")
        sex = input("请输入读者性别：")
        dept = input("请输入读者院系：")
        status = input("请输入读者职业：")
        address = input("请输入读者所在学校：")
        cursor.execute(sql, [reader_id, name, sex, dept, status, address])
        conn.commit()
        connnection_close()
    else:
        print("输入错误,请重新输入！")

# 修改操作
elif number == 3:
    print("ok3")

# 增加数据
elif number == 4:
    print("ok4")
else:
    print("退出程序！")
