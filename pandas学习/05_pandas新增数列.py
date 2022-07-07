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

# 直接赋值
# 给df新加一列,起名为温差,这一列数据由最高温减最低温得到
df['wencha'] = df['bWendu'] - df['yWendu']
# print(df.head(5))
# 练习:查询全年温差小于10度并且最高温大于20度的所有天气数据
# result = df['wencha'] < 10
# result2 = df['bWendu'] >20
# print(df.loc[result&result2])

#