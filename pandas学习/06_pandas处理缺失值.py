#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
# 跳过数据前两行,将第三行数据作为列索引
df = pd.read_excel('./student_excel.xlsx',skiprows=2)
# print(df)

# 1.检测空值isnull() (空为True,不空为False) (notnull空为False不空为True)
# 查看整个表的空值
# print(df.isnull())
# 检测单列空值
# print(df['分数'].isnull())

# 2.删除空值dropna(axis, how, inplace)
# axis:删除的是行还是列,0是行index,1是列columns
# how: any:任何值都会被删除  all: 所有值为空才会删除
# inplace: True / False  是否修改当前对象

# 删除所有空的行
df.dropna(axis=0,how='all',inplace=True)
print(df)
# 删除所有空的列
df.dropna(axis=1,how='all',inplace=True)
print(df)


# 3.填补空值 fillna(values,method,axis,inplace)
# values:是用于填充的值,可以是单个值,可以是字典
# method:ffill 向前填空  bfill 向后填充
df.fillna({'分数':0},inplace=True)
print(df)

df['姓名'] = df['姓名'].fillna(method='ffill')
print(df)

# 4.保存数据  ./保存在当前目录下
df.to_excel('./清洗后的学生数据.xlsx',index = False) #index = False 不加第一列行索引




