#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 位置实参.py
@time: 2020/8/14 10:04
@desc: 
"""


# def describe_pet(animal_type, pet_name):
#     print("I hava a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")
#
#
# describe_pet('hamster', 'harry')
# # 关键字实参来调用函数，使用关键字时，要准确地指定函数定义中的形参名。
# # describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet('dog', 'willie')

# 默认值
def describle_pet(pet_name, animal_type='dog'):
    print("I hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".\n")


# 没有参数时，指定使用默认值
describle_pet('luck')
# 传递参数时，则不使用默认值
describle_pet(pet_name='luck', animal_type='cat')


# test
def make_shirt(size, type='L love Python'):
    print("This T-shirt size is " + size + ".")
    print("type is a " + type + ".\n")


make_shirt('L', 'Hello')
make_shirt('XL')