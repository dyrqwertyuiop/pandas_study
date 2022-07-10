#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
# 读取数据
df = pd.read_csv('./beijing_tianqi_2018.csv')
# 修改数据值
df['bWendu'] = df['bWendu'].str.replace('℃','').astype('int64') #astype转换数据类型相当于python里的int(str())
# print(df['bWendu'])
df['yWendu'] = df['yWendu'].str.replace('℃','').astype('int64')

# 1.series排序 sort_values() 默认是升序
# print(df['aqi'].sort_values())
#sort_values(ascending=False) 降序
# print(df['aqi'].sort_values(ascending=False))

# 按照天气类型升序排序
# print(df['tianqi'].sort_values())

# 2.dataframe的排序
# sort_values(by,ascending = False,inplace = False)
# by是根据哪一个字段(列)进行排序
# ascending = False 降序 True升序 默认是升序
# inplace 是否修改原数据,默认不修改原数据

# dataframe的单列排序
# 按照当日最高温升序排序
# print(df.sort_values(by='bWendu'))
# 按照aqi降序给df排序
# print(df.sort_values(by='aqi',ascending=False))

# dataframe
# 按照最高温度和aqi进行升序排序
# print(df.sort_values(by=['bWendu','aqi']))
# 按照最高温度和aqi进行升序排序
# print(df.sort_values(by=['bWendu','aqi'],ascending=[False,False]))
# 按照最高温度升序,aqi降序
# print(df.sort_values(by=['bWendu','aqi'],ascending=[True,False]))
# 总结:如果两个列或者多个列同时升序/降序,第一个列中所有的数据完全升序/降序,第二个列中的数据不一定完全升序/降序,只有第一列数值相同的时候才会对第二个列中的数据进行排序


