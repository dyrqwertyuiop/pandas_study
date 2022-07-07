#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
# # 数组的索引和切片
# # 生成1~25的等差数组,并把数组改成五行五列
# a = np.arange(1,26).reshape(5,5)
# print(a)
#
# # 数组的索引
# b = np.arange(3,8)
# print(b[2])
# # 多维数组的索引
# # 生成一个1~8的等差数列,并分成4行2列
# c = np.arange(1,9).reshape(4,2)
# print(c[1,0])
#
# # 生成一个1~27的等差数列,并分成3组3行3列
# d = np.arange(1,28).reshape(3,3,3)
# print(d)
# #9
# print(d[0,2,2])
# #17
# print(d[1,2,1])

# # 多维数组的切片
# # 生成一个1~25的等差数列,分成四组每组两行三列,取中间的两组
# a = np.arange(1,25).reshape(4,2,3)
# print(a[1:3])

# # 生成一个1~9的等差数列,分成三行三列
# a = np.arange(1,10).reshape(3,3)
# # 第二列 258
# print(a)
# print(a[...,1])
# # 第二行
# print(a[1,...])
# print(a[1])
