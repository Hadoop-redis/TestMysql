#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: 百度图片采集.py
@time: 2020/8/14 14:45
@desc: 爬虫存在的意义：为了采集大量的数据
    url:https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111pe=2&ie=utf-8&
    爬虫的标准步骤：
    第一步：获取网址信息
    第二部：发送请求
    第三步：提取数据
    第四步，保存数据

    Python使用pep8 的命名规范

    检查网页时：Elements-元素
              Network-
"""
# 发送请求的工具包
import requests
import re
import os

name = input("请输入需要爬取的图片名称：")
# 创建保存图片的目录，以搜索名字命名
os.mkdir("D:\\A\\Code\\Python\\Testmysql\\Python学习\\爬虫\\" + name)
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=" + name + "&cl=2&lm" \
      "=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=" + name + "&s=&se=&tab=&width=&height=&face=0" \
      "&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=3c&1597391934787= "

res = requests.get(url)
print(res.text)

# 提取数据
urls = re.findall('"thumbURL":"(.*?)",', res.text)
print(urls)

for url1 in urls:
    print(url1)

    # 提取文件名
    print(url1.split("/")[-1])

    # .content 将数据变为。。。。
    data = requests.get(url1).content
    print(data)
    # # 保存数据
    with open(name + "/" + url1.split("/")[-1], "wb") as f:
        f.write(data)