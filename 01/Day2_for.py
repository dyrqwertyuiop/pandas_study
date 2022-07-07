#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 循环 for: for 变量名 in 可迭代的对象:执行代码
# for x in '123456':
#     print (x)
# for循环根据可迭代对象的元素个数决定循环次数
# for x in '1234567890':
#     print("你好")

#range():产生一个数据范围(可迭代) 左包右不包
# print (range(1,100,1))#三个参数

# for x in range(1,10,2):
#     print (x)
#
# for x in range(100):
#     print (x)

#选出1-100的2的倍数并且是3的倍数
# 算数运算符:+-*/ //(整除) %(取余) **(次方)
#逻辑运算符:与或非 and or not   and:全真则真,一假则假  or:一真则真,全假为假
# for x in range(1,101):
#     if x % 2 == 0 and x % 3 == 0:
#         print (x)

for x in range(1,101):
    if x % 5 == 0:
        print (x)
