#! /usr/bin/env python
# -*- coding: utf-8 -*-
list1 = ['a','b','c']
list2 = ['A','B']
# a A b B c C
'''
for i in list1:
    print(i)
for j in list2:
    print(j)
'''

# zip函数,zip函数是python的内置函数,zip(a,b)发放的工作原理是创建一个迭代器,该迭代器可以产生出元祖(x,y),这里的x取自a,y取自b. 当其中某个列表中没有元素可以继续访问时,整个迭代过程结束,因此zip的长度取自最短列表长度

for x,y in zip(list1,list2):
    print(x,y)

# 练习:
a=[1,3,5,7]
b=[2,4,6,8]
# 输出12345678
for x,y in zip(a,b):
    print(x)
    print(y)
# 迭代:迭代是通过重复执行的代码处理相似的数据集的过程,并且本次迭代的处理数据要依赖上一次的结果继续往下做,上次的产生的结果是下一次产生结果的初始状态,如果中途有停顿都不算迭代