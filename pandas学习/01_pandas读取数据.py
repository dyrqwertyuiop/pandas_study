#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
# xlsx sql csv
# csv: 是逗号分隔值文件格式,可以用记事本或者Excel打开,他是纯文本数据
# 它是以表格形式存储的
# 读取数据
'''
pd.read_csv(path,sep=',',names= , engine = C,skiprows,nrows)
path:文件路径
sep: 分隔符,默认是逗号
names: 列名,默认是none
header: 表头,默认是infer,可以设置成None
engine: 引擎,默认是C
skiprows: 跳过的行数,默认是全部
nrows:要读取的行数,默认是全部
'''
# df=pd.read_csv('./beijing_tianqi_2018.csv',encoding='utf-8')
# # print(df)
#
# # 读取数据的前几行 head
# print(df.head(10))
# # 读取数据的后几行 tail
# print(df.tail(5))
# # 查看数据的形状
# print(df.shape)
# # 查看数据表的列名
# print(df.columns)
# # 查看表的所有信息
# print(df.info())

# 读取txt文档
# df = pd.read_csv('./新建文本文档.txt',engine='python',sep='',header=None,names=['日期','数据1','数据2'])
# print(df)

# 读取excel文件
df = pd.read_excel('./student.xlsx')
print(df)





