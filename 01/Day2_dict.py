#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 字典:键值对组成
dict_1={"宋悦":"小狗狗",'杜艳荣':'小猫猫','田家维':'小脑斧'}
# 查:
# print(dict_1['宋悦']) #不可切片
# for x in dict_1:
#     print(x)
# 遍历字典
# 遍历键
for x in dict_1.values():
    print(x) #取出dict_1的所有值

for x in dict_1.keys():
    print(x)#取出dict_1的所有键

for x in dict_1.items():
    print(x)#取出dict_1的所有

# 增:
dict_1['class'] = 28
print(dict_1)

dict_1['class'] = 29
print(dict_1) #当键存在时,修改相应的值

# 删:
dict_1.pop('宋悦')
print(dict_1)

for x,y in dict_1.items():
    print(x,y)

# def 名字(括号里都是形参)
# 自己写的都是实参
# 类:具有相同的属性及方法

# 1.find()#返回找到的第一个值的索引,若不存在返回-1
name = '张三,李四,王五,赵六,田七'
print(name.find('九'))
# 2.index() 返回找到的第一个值的索引,若不存在报错
print(name.index('王'))

# count() 计数
print(name.count('王'))

# replace()
print(name.replace('田七','汪洋'))

# len() 长度(元素的长度)

