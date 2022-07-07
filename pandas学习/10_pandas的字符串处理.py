#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pandas的字符串处理
# 1.使用方法: 先获取series的str属性,然后在属性上调用函数
# 2.只能在字符串列使用,不能在数字列使用
# 3.dataframe没有字符串属性
# 4.series.str不是python中字符串的方法,而是一个属性,pandas和python中的str是两回事

import pandas as pd
df = pd.read_csv('./beijing_tianqi_2018.csv')
# print(df.head(5))

# # 将df中的最高温和最低温的摄氏度去掉
# # replace功能
# df['bWendu'] = df['bWendu'].str.replace('℃','')
# df['yWendu'] = df['yWendu'].str.replace('℃','')
# print(df.head(5))
# # 将风力中的'-'换成'到'
# df['fengli'] = df['fengli'].str.replace('-','到')
# print(df.head(5))
#
# # isnumeric 判断series中的数据是不是数字,是的返回True,不是返回False
# print(df['fengli'].str.isnumeric())
#
# # len() 返回series中字符串的长度
# print(df['fengli'].str.len())

# startswith() 检测字符串是不是以xxx开头,是的返回True,不是返回False
# endswith() 检测字符串是不是以xxx结尾,是的返回True,不是返回False
# 查询2018年一月的天气数据
print(df['ymd'].str.startswith('2018-01'))
print(df.loc[df['ymd'].str.startswith('2018-01')])
# 查询2018年每个月15号的天气数据
print(df.loc[df['ymd'].str.endswith('15')])
# 练习:用两种方法查询2018年北京刮东北风的天气
print(df.loc[df['fengxiang'].str.startswith('东北')])
print(df.loc[df['fengxiang'] == '东北风'])

