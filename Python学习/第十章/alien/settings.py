#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: settings.py
@time: 2020/8/17 16:10
@desc: 
"""


class Settings():
    """存储《alien》的所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (206, 222, 195)

        # 飞船的设置
        self.ship_speed_factor = 1.5


