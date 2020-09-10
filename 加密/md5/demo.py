#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: demo.py
@time: 2020/8/28 14:06
@desc: 实现建议加密注册登录
"""

# 导入加密算法
import hashlib
username = input('username:')
pwd = input('pwd:')
# 初始化加密模板
md5 = hashlib.md5()
# 添加要加密的字节
md5.update(pwd.encode('utf-8'))
# 进行加密
m = md5.hexdigest()
print(m)


# 创建文件
f = open('da123.txt', 'w', encoding='utf-8')
# {username}:和{m}之间不能留空格，否则不能登录
f.write(f'{username}:{m}')
f.close()


# 登录
username1 = input('username:')
pwd1 = input('pwd:')
md5 = hashlib.md5()
md5.update(pwd1.encode('utf-8'))
m1 = md5.hexdigest()
print(m1)


# 打开文件
f = open('da123.txt', 'r', encoding='utf-8')
for i in f:
    username, m = i.strip().split(":")
    if username == username1 and m1 == m:
        print("登录成功")
        break
    else:
        print("用户名或密码错误请重新登录")

f.close()
