#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: change.py
@time: 2020/8/11 10:38
@desc: 修改数据
"""
import os
import sys
import pymysql


class transferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, sourceID, targetID, money):
        #   其他函数中若是有错会抛出异常而被检测到。
        try:
            self.checkIdAvailable(sourceID)
            self.checkIdAvailable(targetID)
            self.ifEnoughMoney(sourceID, money)
            self.reduceMoney(sourceID, money)
            self.addMoney(targetID, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def checkIdAvailable(self, ID):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where id = %d" % ID  # select语句判断可以用len(rs)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:  # 数据库类思想的报错模式，检查操作对数据库的影响条目。没有达到目标，抛出异常
                raise Exception("账号 %d 不存在" % ID)
        finally:
            cursor.close()

    def ifEnoughMoney(self, ID, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where id = %d and money>=%d" % (ID, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %d 不存在 %d Yuan" % (ID, money))
        finally:
            cursor.close()

    def reduceMoney(self, ID, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money-%d where id=%d" % (money, ID)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("失败减钱")
        finally:
            cursor.close()

    def addMoney(self, ID, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money+%d where id=%d" % (money, ID)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("失败加款")
        finally:
            cursor.close()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        sourceID = int(sys.argv[1])
        targetID = int(sys.argv[2])
        money = int(sys.argv[3])

        conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='dyx240030', db='imooc', charset='utf8')
        trMoney = transferMoney(conn)

        try:
            trMoney.transfer(sourceID, targetID, money)
        except Exception as e:
            print("出现问题" + str(e))
        finally:
            conn.close()