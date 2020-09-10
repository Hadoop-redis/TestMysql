#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test.py
@time: 2020/8/11 13:50
@desc: https://www.jb51.net/article/116975.htm
"""
import pymysql

class MySQLCommand(object):
    def __init__(self, host, port, user, passwd, db, table):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.table = table

    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port,
                                        user=self.user, passwd=self.passwd,
                                        db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysqld error.')

    def queryMysql(self):
        sql = "select * from " + self.table

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            print(row)
        except:
            print(sql + ' execute failed.')

    def insertMysql(self, id, name, sex):
        sql = "insert into " + self.table + "values(" + id + "," + "'" + name + "'," + "'" + sex + "')"
        try:
            self.cursor.execute(sql)
        except:
            print("insert failed.")

    def updateMysqlSN(self, name, sex):
        sql = "update " + self.table + " set sex='" + sex + "'" + " WHERE name='" + name + "'"
        print("update sn:" + sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()