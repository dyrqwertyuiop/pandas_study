#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 列表 list:[]
# 列表可以存任意数据类型的数据
# list_1 = [1,'123',1.0,True,[],()]
# list_2 = list()
# print(list_1)
# print(list_2)

# 列表的增删改查
# 查:列表存在索引,有序
import time

name = ['张三','李四','王五','赵六六','田七']
# print(name[2])
# print(name[1::2])
# 增: append()
# name.append('狗八')
# print(name)

# insert()
# name.insert(2,'杜杜杜') #索引为2的位置
# print(name)

# 删:remone()
# name.remove('狗八')
# print(name)

# pop()
# name.pop(2)
# print(name)

# del 删除范围
del name[0:1] #左包右不包
# print(name)

# 改
# name[2]='赵六'
# print(name)

# 列表的遍历
# for i in name:
#     time.sleep(1)
#     print(i)

name.append('张三丰')
name.append('张三')
print(name)

for x in name:
    if x.startswith('张'):
        print(x)

import random
name_list = random.choice(['田家维','姚远','黄进岳','杜艳荣','姜涛', '闫明','黄辉','娄家伟','郭钟民','秦志阳','吴益通','宋旺旺'])
print(name_list)

b=random.randint(1,10) #全包
print(b)

#随机跟电脑猜拳,可以无限次数比赛直到赢为止
#随机跟电脑猜拳,可以比5次比赛,要求显示输赢的次数


