#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_excel('./清洗后的学生数据.xlsx')
print(df)
# 检测姓名这一列是否存在重复,是返回True,不是返回False
# duplicated:检测重复值
print(df.duplicated('姓名'))
# 删除重复值drop_duplicates
# 删除具有重复值的这一行
print(df.drop_duplicates('姓名'))

# 检测分数这一列是否存在重复,是返回True,不是返回False
print(df.duplicated('分数'))
# 删除分数具有重复值的这一行
print(df.drop_duplicates('分数'))
