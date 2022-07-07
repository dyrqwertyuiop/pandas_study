#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
numpy 主要用于科学计算 支持多维度数组和矩阵的计算,运行效率高,是机器学习的框架基础
'''
import numpy as np
# 生成一个一维数组(数组是numpy里特有的数组里只有数字无其他符号,可以增大计算效率)
list1 = [1,2,3,4,5,6]
a = np.array(list1)
print(a)

# 指定数组的维度 ndmin
b = np.array(list1,ndmin=4)
print(b)

# 获取数组维度,数组秩
print(b.ndim)

# 生成等差数组 arange()
c = np.arange(1,5)
print(c)
# 练习:生成表示一天24小时的数组
d = np.arange(1,25)
print(d)
# 练习:生成表示一天24小时偶数的数组
e = np.arange(2,25,2)
print(e)

#调整数组大小 reshape(m行,n列) reshape(s堆,m行,n列) f的值=s*m*n
# reshape功能的数字积 = 数组数字个数
f = np.arange(1,25)
f1 = f.reshape(4,6)
print(f1)

f2 = f.reshape(3,4,2)
print(f2)

# 练习: 生成一个1-100的等差数组,把这个数组变成4组五行五列
h = np.arange(1,101)
f3 = h.reshape(4,5,5)
print(f3)

# 通过数组的shape属性来得到它的形状
print(f3.shape)
# 通过数组的size属性来得到数组元素个数
print(f3.size)
# ones:创建一个指定大小的数组并用1填充
g = np.ones([3,4,2])  #中括号里是数组形状
print(g)
# zeros:创建一个指定大小的数组并用0填充
i = np.zeros([2,4,7])
print(i)
# asarray:可以将元组和列表转换成数组
t = (1,2,3)
at = np.asarray(t)
print(at)

l = [1,2,3]
al = np.asarray(l)
print(al)

tl = [(1,2,3),(4,5,6)]
atl = np.asarray(tl)
print(atl)