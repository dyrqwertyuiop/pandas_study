#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time #选中time,双击ctrl+B即可看解释
import random

# 循环while
# age = int(input('请输入您的年龄:'))
# i = 0
# while age > 18:
#     print ('已成年')
#     i = i + 1
#     if i==6:
#         print ("跳出循环")
#         break  #跳出全部循环

#continue: 跳出当前循环
# a = 'python'
# for x in a:
#     if x == 'h':
#         continue
#     print(x)


# 模拟生活中密码输入
# a=0
# while True:
#     user_name = input('请输入您的账号:')
#     if user_name == 'lksj':
#         while True:
#             pass_number = input('请输入您的密码:')
#             if pass_number == '123456':
#                 print('登录成功')
#                 break
#             else:
#                 a=a+1
#                 print(f'密码错误,您还能再输入{3-a}次')
#                 if a == 3:
#                     print('账号冻结')
#                     break
#         break
#     else:
#         print('账号错误')

# 输入账号密码 总共可以错3次,然后第四次冻结账号

# 总结 for对比while
# 1.for循环更注重次数,while更注重循环条件
# 2.for循环能做的while都能做,反之不然

a='123456789'
for x in a:
    time.sleep(1)
    print(x)