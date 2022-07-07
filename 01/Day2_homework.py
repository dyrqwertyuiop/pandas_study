#! /usr/bin/env python
# -*- coding: utf-8 -*-

#随机跟电脑猜拳,可以无限次数比赛直到赢为止
import random

# while True:
#     i = input("请输入石头或剪刀或布:")
#     t = random.choice(['石头','剪刀','布'])
#     print("电脑出"+t)
#     if i == t :
#         print('平局')
#     elif i == '布' and  t == '剪刀' or  i == '剪刀' and t == '石头' or i == '石头' and t == '布' :
#         print('你输了')
#     else:
#         print('你赢了!')
#         break

#随机跟电脑猜拳,可以比5次比赛,要求显示输赢的次数
# a = 0
# b = 0
# c = 0
# while True:
#     a = a + 1
#     i = input("请输入石头或剪刀或布:")
#     t = random.choice(['石头', '剪刀', '布'])
#     print("电脑出" + t)
#     if a < 6:
#         if i == t:
#             print('平局')
#         elif i == '布' and t == '剪刀' or i == '剪刀' and t == '石头' or i == '石头' and t == '布':
#             b = b + 1
#             print(f'你输了{b}次')
#         elif i == '布' and t == '石头' or i == '剪刀' and t == '布' or i == '石头' and t == '剪刀':
#             c = c + 1
#             print(f'你赢了{c}次')
#     else:
#         break


# 输出九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        x=int(str(x))
        y=int(str(y))
        z=x*y
        print(f'{x}*{y}={z}')


