#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: year.py
@time: 2020/8/31 8:59
@desc: 判断用户输入的年份是否为闰年
    1、问题分析：能被4整除但不能被100整除的年份为普通闰年，
    能被400则会那个出的年份为世纪闰年。
    2、算法分析：输入一个数，险判断如果是400的整数倍，则满足；如果不是400的倍数，
    再判断如果该数能够被4整除，却不能被100整除，则满足。
"""
# while True:
#     n = int(input('请输入年份：'))
#     if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
#         print('{0}是闰年'.format(n))
#     else:
#         print('{0}不是闰年'.format(n))

# 使用第三方库
# import calendar
#
# n = int(input("请输入年份："))
# year = calendar.isleap(n)
#
# if year == True:
#     print("{0}是闰年".format(n))
# else:
#     print("{0}不是闰年".format(n))

# print('{:,}'.format(123456789))
# print('my name is {0},{0} age is {1}'.format('wang', 10))

# 对于数组
# msg = ['wang', 10]
# print('my name is {0},{0} age is {1}'.format(*msg))
#
# # 对于字典
# msg = {'name': 'wang', 'age': 10}
# xx = 'my name is {name},{name} age is {age}'.format(**msg)
# print(xx)
#
# nn = '{:*^20}'.format('你好')
# print(nn)

temp = "Zc"
