#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pandas中的数据框
# 1.dataframe:表格型的数据类型,每一列都可以是不同的值(整数,字符串,布尔..)
# 既有行索引index,也有列索引columns,创建dataframe最简单的方法就是读取文件,可以看成是series构成的

# 2.series:一维数据,只有一行或一列,只有行索引
import pandas as pd
# 创建series注意大写
# s = pd.Series(['dog','bie','pig','cat'])
# print(s)
# # 创建具有标签的索引
s1 = pd.Series(['dog','bie','pig','cat'],index=['a','b','c','d'])
# print(s1)
# # 获取series的索引
# print(s1.index)
# # 获取series的值
# print(s1.values)
# =====================================
# 根据字典创建dataframe
data = {
    'ID':[1,2,3,4],
    'name':['dog','bie','pig','cat'],
    'score':[50,60,70,80]
}
df = pd.DataFrame(data)
# print(df)

# dataframe的数据查询
# 查询一列
print(df['name'])
# 查询多列
print(df[['name','score']])

# 查询一行
print(df.iloc[1])
# 查询多行可用切片
print(df.iloc[1:3])
