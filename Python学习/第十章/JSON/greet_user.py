#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: greet_user.py
@time: 2020/8/17 14:56
@desc: 
"""
import json


# filename = 'username.json'
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + "!")
def get_stored_username():
    """如果用户存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        # username = input("What's your name?")
        # filename = 'username.json'
        # with open(filename, 'w') as f_obj:
        print("We'll remember you come back, " + username + "!")


greet_user()
