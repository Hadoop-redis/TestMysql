#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: alien_invasion.py
@time: 2020/8/17 16:02
@desc: 创建一个空的Pygame窗口
"""
import sys
import pygame
from 第十章.alien.settings import Settings
from 第十章.alien.ship import Ship
import 第十章.alien.game_functions as gf


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个飞船
    ship = Ship(ai_settings, screen)

    # 设置背景颜色
    bg_color = (206, 222, 195)

    """开始游戏的住循环"""
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
