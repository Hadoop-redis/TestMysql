#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 笔记本防盗.py
@time: 2020/8/17 15:18
@desc: 笔记本防盗  可以自动调用摄像头设备工具
        自动发送邮箱装置   电脑OS操作系统
"""
import cv2
import os   # 图片操作系统
import smtpd


def get_photo():
    cap = cv2.VideoCapture(0)  # 开启摄像头 0 null
    f, frame = cap.read()  # 保存本地照片
    cv2.imwrite('image.jpg', frame)  # 本地文件
    cap.release()   # 关闭摄像头


if __name__ == '__main__':
    get_photo()