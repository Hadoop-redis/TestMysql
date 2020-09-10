#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 8-1.py
@time: 2020/8/14 9:50
@desc: 
"""


# username：形参   jessica：实参
def greet_user(username):
    print("Hello " + username.title() + "!")


greet_user('jessica')


def display_message():
    print("定义函数的学习！")


display_message()


def favorite_book(bookname):
    print("One of my favorite books is " + bookname.title() + " in Wonderland.")


favorite_book('《python从入门到实践》')
