#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: test1.py
@time: 2020/8/11 14:13
@desc: 
"""
import pymysql.cursors


class Database:
    connected = False
    __conn = None

    # 构造函数，初始化时直接连接数据库
    def __init__(self, conf):
        if type(conf) is not dict:
            print('error：参数不是字典类型！')
        else:
            for key in ['host', 'port', 'user', 'pw', 'db']:
                if key not in conf.keys():
                    print('error：参数字典缺少 %s' % key)
            if 'charset' not in conf.keys():
                conf['charset'] = 'utf8'
        try:
            self.__conn = pymysql.connect(
                host=conf['host'],
                port=conf['port'],
                user=conf['user'],
                passwd=conf['pw'],
                db=conf['db'],
                charset=conf['charset'],
                cursorclass=pymysql.cursors.DictCursor)
            self.connected = True
        except pymysql.Error as e:
            print('数据库连接失败：', end='')

    # 插入数据
    def insert(self, table, val_obj):
        sql_top = "insert into " + table + ' ('
        sql_tail = ') values ('
        try:
            for key, val in val_obj.items():
                sql_top += key + ','
                sql_tail += val + ','
            sql = sql_top[:-1] + sql_tail[:-1] + ')'
            with self.__conn.cursor() as cursor:
                cursor.excute(sql)
            self.__conn.commit()
            return self.__conn.insert_id()
        except pymysql.Error as e:
            self.__conn.rollback()
            return False

    # 更新数据到数据表
    def update(self, table, val_obj, range_str):
        sql = 'update ' + table + 'set'
        try:
            for key, val in val_obj.items():
                sql += key + '=' + val + ','
            sql = sql[:-1] + ' where ' + range_str
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.Error as e:
            self.__conn.rollback()
            return False

    # 删除数据在数据表中
    def delete(self, table, range_str):
        sql = 'delete from ' + table + ' where ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.rowcount
        except pymysql.Error as e:
            self.__conn.rollback()
            return False

    # 查询唯一数据在数据表中
    def sqlect_one(self, table, factor_str, field='*'):
        sql = 'select ' + field + ' from ' + table + ' where ' + factor_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]
        except pymysql.Error as e:
            return False

    # 查询多条数据在数据表中
    def select_more(self, table, range_str, field='*'):
        sql = 'select' + field + 'from' + table + ' where ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()
        except pymysql.Error as e:
            return False

    # 统计某表某条件下的总行数
    def count(self, table, range_str='1'):
        sql = 'select count(*) res from ' + table + ' where ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]['res']
        except pymysql.Error as e:
            return False

    # 统计某字段（或字段计算公式）的合计值
    def sum(self, table, field, range_str='1'):
        sql = 'select sum(' + field + ') as res from ' + table + 'where ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]['res']
        except pymysql.Error as e:
            return False

    # 销毁对象时关闭数据库连接
    def __del__(self):
        try:
            self.__conn.close()
        except pymysql.Error as e:
            pass

    # 关闭数据库连接
    def close(self):
        self.__del__()