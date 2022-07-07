#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
# 读取数据
df = pd.read_csv('./beijing_tianqi_2018.csv')
# 设置索引值drop:是否删除原数列
df = df.set_index('ymd',drop = False)  #把日期设置为行索引
# print(df.head(5))
# # 查询2018年10月1日的天气
# print(df.loc['2018-10-01'])
# print(df.loc['2018-03-15','yWendu'])
# print(df.loc['2018-11-03','fengli'])
# print(df.loc['2018-03-18','bWendu'])

# 一行多列
# 例子:查询18年3月15日的最低温度,最高温,风力
# print(df.loc['2018-03-15',['yWendu','bWendu','fengli']])
#
# print(df.loc['2018-03-15',['bWendu','fengli','fengxiang']])
# print(df.loc['2018-09-30',['yWendu','tianqi','aqi']])

# print(df.columns) #查询列名

# 多行多列
# 2018年2月最后两天的最高温和最低温
# print(df.loc[['2018-02-27','2018-02-28'],['bWendu','yWendu']])
#
# # 3月最后两天的风力和风向
# print(df.loc[['2018-03-30','2018-03-31'],['fengli','fengxiang']])
#
#
# # 区间查询
# # 查询十月全部日期的最高温和最低温
# print(df.loc['2018-10-01':'2018-10-31',['bWendu','yWendu']])
# # 查询18年十一假期的最高温和风力
# print(df.loc['2018-10-01':'2018-10-07',['bWendu','fengli']])

# 查询18年十一假期的除了温度以外的天气信息
# print(df.loc['2018-10-01':'2018-10-07','tianqi':'aqiLevel'])

# 条件查询
# 查询全年空气质量低于40的天气数据
# 怎么做:只需要把满足条件的行索引找出来,满足返回True,不满足返回False
# print(df['aqi']<40)
# result = df['aqi']<40
# print(df.loc[result])

# 查询2018年北京全年最高温为30度的天气数据
# result = df['bWendu'] == '30℃'
# print(df.loc[result])

# result = df['aqiInfo'] == '良'
# print(df.loc[result])
#
# result = df['fengli'] == '1级'
# print(df.loc[result])

# 多条件查询
# 查询全年最高温为23度,并且空气质量信息为优的天气数据
# result1 = df['bWendu'] == '23℃'
# result2 = df['aqiInfo'] == '优'
# print(df.loc[result1&result2])

# 练习:查询全年空气质量指数小于50,空气质量为优
# result1 = df['aqi'] < 50
# result2 = df['aqiInfo'] == '优'
# print(df.loc[result1&result2])



