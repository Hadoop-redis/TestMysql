#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 使用任意数量的关键字实参.py
@time: 2020/8/14 13:51
@desc: 
"""


# **user_info:创建一个名为user_info的空字典，并讲收到的所有名称-值对都封装到这个字典中。
def build_profile(first, last, **user_info):
    # 创建一个字典，其中包含我们知道的有关用户的一切
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
