#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 9-1.py
@time: 2020/8/16 12:33
@desc: 餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：
restaurant_name 和 cuisine_type。创建一个名为 describe_restaurant()的方法和一个
名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，
指出餐馆正在营业。
根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述
两个方法。
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurnt name is " + self.restaurant_name + ".")
        print("This restaurant is open " + self.cuisine_type + "!")

    def open_restaurant(self):
        print("This restaurant is open!")


restaurant = Restaurant("HuoGuo", 'Chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\nHello " + restaurant.restaurant_name.title())
print("Hello " + restaurant.cuisine_type.title())