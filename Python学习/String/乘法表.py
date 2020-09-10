#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 乘法表.py
@time: 2020/8/10 15:50
@desc: 
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d"%(j, i, j * i), end=" \t")
    print("")

print("======================================================================")

n = 1
sum = 1
while n <= 9:
    i = 1
    while i <= n:
        sum = i * n
        print('%d*%d=%d' % (i, n, sum), end=" \t")
        i = i + 1
    print('')
    n = n + 1