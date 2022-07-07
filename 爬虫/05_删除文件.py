#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
# //:全局变量
# ./:当前路径
# os.listdir() 用户返回指定文件夹的文件或者文件夹名字的列表
list = os.listdir('./')
for dir in list:
    # print(dir)
    if dir.endswith('.jpg'):
        os.remove(dir)
