#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test1.py
@time: 2020/8/13 13:56
@desc: 
"""
import pymysql
import re

conn = pymysql.connect(host="192.168.11.128",
                       user="root",
                       password="root",
                       database="Linux",
                       charset="utf8")
cursor = conn.cursor()


# 结束模块
def connnection_close():
    cursor.close()
    conn.close()


# 限制输入的数为整数
print("========================载入数据库操作========================")
print("1、进入查询操作")
print("2、插入数据！")
print("3、修改数据！")
print("4、删除数据")
print("5、退出程序！")

while True:
    time = 0
    number = input("请输操作选项：")
    while not re.findall('^[1-5]+$', number):
        number = input("输入错误，请重新输入：")
    print(number)
    break

# 查询操作
if number == '1':
    print("==================表列表==================")
    cursor.execute("show tables")
    # x = cursor.fetchall()
    # for i in x:
    #     print(i)
    print(cursor.fetchall())
    table = input("请输入要查询的表名：")
    sql = "select * from " + table + ";"
    try:
        cursor.execute(sql)
        ret = cursor.fetchall()
        # print(ret)
        for i in ret:
            print(i)
            # connnection_close()
    except Exception as e:
        print("错误信息：%s" % str(e))
    finally:
        connnection_close()


# 插入操作
elif number == '2':
    try:
        print("==================表列表==================")
        cursor.execute("show tables")
        # x = cursor.fetchall()
        # for i in x:
        #     print(i)
        print(cursor.fetchall())
        table = input("请输入要插入数据的表名：")
        # print("==================表结构==================")
        # cursor.execute("desc " + table + ";")
        # ret1 = cursor.fetchall()
        # for a in ret1:
        #     print(a)
        if table == "information":
            print("==========================需要插入的字段和类型========================== \n"
                  "ip地址--varchar(16)：ip,           计算机名--varchar(20)：name \n"
                  "内存大小--int(3)：memory_size,      操作位数--int(2)：operation_bits \n"
                  "磁盘大小--int(4)：disk_size,        注释--varchar(200)：notes")
            sql = "INSERT INTO information VALUES(%s, %s, %s, %s, %s, %s);"
            ip = input("请输ip地址:")
            name = input("请输入计算机名:")
            memory_size = input("请输入内存大小:")
            operation_bits = input("请输入操作位数:")
            disk_size = input("请输入磁盘大小:")
            notes = input("注释:")
            # try:
            cursor.execute(sql, [ip, name, memory_size, operation_bits, disk_size, notes])
            conn.commit()

        elif table == "network":
            print("==========================需要插入的字段和类型========================== \n"
                  "读者编号--varchar(20)：name,          书号--varchar(10)：connection_type \n"
                  "时间--int(3)：processor_amount,       注释--int(3)：kernel_amout")
            sql = "INSERT INTO network VALUES(%s, %s, %s, %s);"
            name = input("请输入计算机名：")
            connection_type = input("请输入网络连接方式：")
            processor_amount = input("请输入处理器数量：")
            kernel_amout = input("请输入处理器内核数量：")
            # try:
            cursor.execute(sql, [name, connection_type, processor_amount, kernel_amout])
            conn.commit()
            # except Exception as e:
            #     print("错误信息：%s" % str(e))
            #     conn.rollback()
            # finally:
            #     connnection_close()
        else:
            print("输入错误，请重新操作！")
    except Exception as e:
        print("错误信息： %s" % str(e))
        conn.rollback()
    finally:
        connnection_close()

# 修改操作
elif number == '3':
    print("===================修改数据===================")
    cursor.execute("show tables")
    # x = cursor.fetchall()
    # for i in x:
    #     print(i)
    print(cursor.fetchall())
    table = input("请输入要修改数据的表名：")
    # sql = "select * from " + table + ";"
    cursor.execute("select * from " + table + ";")
    ret = cursor.fetchall()
    # print(ret)
    for i in ret:
        print(i)

    test = input("请输入要修改的字段：")
    test1 = input("请输入要修改的参数：")
    test2 = input("请输入要修改数据的虚拟机的名称：")
    sql1 = "update " + table + " set " + test + "=" + test1 + " where name='" + test2 + "';"
    try:
        cursor.execute(sql1)
        conn.commit()
    except Exception as e:
        print("错误信息：%s" % str(e))
        conn.rollback()
    finally:
        connnection_close()

# 删除数据
elif number == '4':
    print("==================删除某列数据==================")
    cursor.execute("show tables")
    print(cursor.fetchall())
    table = input("请输入要删除数据的表名：")
    cursor.execute("select * from " + table + ";")
    ret = cursor.fetchall()
    for r in ret:
        print(r)

    ip = input("请输入需要删除数据所在的列的虚拟机的ip地址：")
    sql = "delete from " + table + " where ip='" + ip + "';"
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("错误信息：%s" % str(e))
        conn.rollback()
    finally:
        connnection_close()

else:
    try:
        connnection_close()
    except Exception as e:
        print("退出程序----------: %s" % str(e))
    finally:
        print("退出程序！")