#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pandas 索引的用途
# 1.方便查询数据
# 2.提高查询效率
# 3.自动进行数据对齐
import pandas as pd
df = pd.read_csv(r'./ratings.csv')
# print(df.info())
#查询用户ID为11的所有用户信息
# 法一:扫描了整个dataframe,效率不高
print(df.head(5))
print(df['userId'] == 11)
print(df.loc[df['userId'] == 11])
# 法二:将要查询的userId作为索引
df.set_index('userId', inplace=True, drop=False)
print(df)
print(df.loc[11])
#查询用户ID为500
print(df.loc[500])

# 数据对齐
s1 = pd.Series([2,3,4,],index=['a','b','c'])
s2 = pd.Series([2,3,4,],index=['b','c','d'])
print(s1)
print(s2)
print(s1+s2)

s3 = pd.Series([2,3,4],index=['a','b','c'])
s4 = pd.Series([2,3,4],index=['c','a','b'])
print(s3+s4)




