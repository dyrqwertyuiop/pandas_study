#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pandas数据合并
# 功能:批量合并形同格式的Excel,也可以给表添加列
# 语法:concat(obj,axis=0,join='inner',ignore_index=False)
# obj:一个列表[df1,series] 列表里可以添加需要合并的df或者series
# axis:按照行合并还是列合并
# join:对齐方式,默认的对齐方式是outer,也可以是inner
# ignore_index:是否忽略原来的索引
import pandas as pd
import numpy as np
df1 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    "B":['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'E':['E0','E1','E2','E3'],
})

df2 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    "B":['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3'],
})
print(df1)
print(df2)
# 默认的concat合并
print(pd.concat([df1,df2]))
# 忽略原来的索引
print(pd.concat([df1,df2],ignore_index=True))
# 过滤掉不匹配的列
print(pd.concat([df1,df2],ignore_index=True,join='inner'))
# 给表添加列
s = pd.Series([1,2,3,4],name='F')
print(s)
print(pd.concat([df1,s],axis=1))






