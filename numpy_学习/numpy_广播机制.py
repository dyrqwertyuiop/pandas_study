#! /usr/bin/env python
# -*- coding: utf-8 -*-

# numpy中的广播机制是通过numpy产生的不同性质的数组与数值之间的计算方式,
# 使数组的算术运算运用到该数组的每一个元素上

import numpy as np
# # 单个数组的广播
# a = np.arange(1,10)
# print(a)
# print(a*10)
# # 注意和列表的区别
# b=[1,2,3]
# print(b*10)

# 多个数组的广播
# 当数组形状不同进行运算时,就会触发广播机制
# 创建一个c数组为1~12的等差数列,并分成2组,每组两行三列
c = np.arange(1,13).reshape(2,2,3)
print('数组c')
print(c)

# 创建一个d数组为1~6的等差数列,两行三列
d = np.arange(1,7).reshape(2,3)
print('数组d')
print(d)

print('相乘结果')
print(c*d)

