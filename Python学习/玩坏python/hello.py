#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: hello.py
@time: 2020/8/14 14:39
@desc: 
"""
import os
import time

print('**********************')
print('  欢迎来到猪猪游戏')
print('**********************\n')
key = input("请问你是天才还是猪：")

if key == "猪":
    time.sleep(1.5)
    print('明白就好啦\n')
    time.sleep(3)
    print('没事的，来抱一哈\n')

else:
    print("既然如此...")
    time.sleep(3)
    print("本天才就要制裁你电脑，啊哈哈~~~~~")
    os.system('shutdown -r -t 10')
time.sleep(10)
