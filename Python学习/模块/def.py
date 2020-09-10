#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: def.py
@time: 2020/8/10 16:44
@desc: 
"""
Money = 2000


def AddMoney():
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)
