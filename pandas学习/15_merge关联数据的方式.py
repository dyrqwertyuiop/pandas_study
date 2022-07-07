#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 数据关联方式
# inner: 左右都有才会出现在结果里(交集)
# outer:左右有的都会出现在结果中,如果没有匹配返回空(并集)
# right:右边的数据都会出现在结果中,左边无法匹配的返回空
# left:左边的数据都会出现在结果中,右边无法匹配的返回空
import pandas as pd
import numpy as np
# 生成一个四行三列从1~12的等差数列,并转换为df命名为left,列名为Key,A,B
# 生成一个四行三列从1~12的等差数列,并转换为df命名为left,列名为Key,C,B

left = pd.DataFrame(np.arange(1,13).reshape(4,3),columns=['Key','A','B'])
right = pd.DataFrame(np.arange(1,13).reshape(4,3),columns=['Key','C','B'])


# 给left新加一列D,列中的值为D1,D2,D3,D4
# 给right新加一列D,列中的值为D1,D2,D5,D6
left['D']=['D1','D2','D3','D4']
right['D']=['D1','D2','D5','D6']
print (left)
print (right)

# inner对齐(默认的连接方式)
print(pd.merge(left,right,on='D',how='inner'))
# outer对齐
print(pd.merge(left,right,on='D',how='outer'))
# left对齐
print(pd.merge(left,right,on='D',how='left'))
# right对齐
print(pd.merge(left,right,on='D',how='right'))

