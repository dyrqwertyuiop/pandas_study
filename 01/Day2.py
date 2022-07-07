#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 判断:if
# 格式1: if + 条件:执行代码
# age = int(input("请输入您的年龄:"))
# if age > 18:
#     print ('可以去网吧')
# print ('不可以去网吧')    # python依靠缩进识别代码块
# # 比较运算符: > < <= >= != ==

# tall = int(input("请输入您的身高:"))
# if tall > 165:
#     print ('高')
# print ('不高')

# 格式2: if + 条件: 执行代码1 else: 执行代码2
# height = int(input("请输入您的身高:"))
# if height > 165:
#     print ('gao')
# else:
#     print ('bugao')

#格式3: if + 条件1: 执行代码1  elif + 条件2:执行代码2......else:执行代码N
# 在没有特殊的情况下,python执行顺序为:从上至下,从左到右
# score = int(input('学生成绩为:'))
# if score > 90:
#     print ('A')
# elif 80 <= score <= 95:
#     print ('B')
# else :
#     print ('C')

#格式4: if 的嵌套
user_name = input('请输入您的账号:')
if user_name =='lksj':
    pass_number=input('请输入您的密码:')
    if pass_number == '123456':
        print ('登录成功')
    else:
        print ('登录错误')
else:
    print ('账号错误')