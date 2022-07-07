#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
# 读取数据
df = pd.read_csv('./beijing_tianqi_2018.csv')
# print(df)
# 修改数据值
# 找到目标列(Series)
s = df['bWendu']
# print(s)
# 找到s中的字符串
'''
str = df['bWendu'] #['3℃','2℃ ','2℃'.......  ]
strresult = str.replace('℃','') #['3','2','2'........]
result = strresult.astype('int64') #[3,2,2.....]
'''
# 修改数据值
df['bWendu'] = df['bWendu'].str.replace('℃','').astype('int64') #astype转换数据类型相当于python里的int(str())
# print(df['bWendu'])
df['yWendu'] = df['yWendu'].str.replace('℃','').astype('int64')
# print(df['yWendu'])

# 查询单个数据值
# 1.平均值 mean
# print(df['yWendu'].mean())
# 2.最小值 min
# print(df['yWendu'].min())
# 3.最大值 max
# print(df['yWendu'].max())
# 4.中位数 median
# print(df['bWendu'].median())
# 5.按值计数values_counts()
# 北京2018年不同风力分别出现了多少次
# print(df['fengli'].value_counts())
# 相关系数 print(df.corr())
# 协方差  print(df.cov())
# 标准差 print(df.std())
import pandas as pd





