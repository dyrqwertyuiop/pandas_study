#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
# 创建一个四行四列的1~16等差数组,并把它转换为df,列名为ABCD

df = pd.DataFrame(np.arange(1,17).reshape(4,4),columns=['A','B','C','D'])
print(df)

# 删除一行
# 删除第一行
print(df.drop(0,axis=0))

# 删除一列
# 删除'B'一列
print(df.drop('B',axis=1))

# 求每一行的平均值
print(df.mean(axis=1))
# 求每一列的平均值
print(df.mean(axis=0))
# 求每一行的和
print(df.sum(axis=1))
# 求每一列的和
print(df.sum(axis=0))

# 新增一行行索引为4,计算每一列的和
df.loc[4] = df.sum(axis=0)
print(df)

# 新加一列sum_values,计算每一行的和
df['sum_values'] = df.sum(axis=1)
print(df)

