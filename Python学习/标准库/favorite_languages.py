#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: favorite_languages.py
@time: 2020/8/17 10:47
@desc: 
"""
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarch'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " + language.title() +'.')