#! /usr/bin/env python
# -*- coding: utf-8 -*-
# lambda:匿名函数,之一类无需定义的子函数或者子程序
def sum(x,y):
    return x+y
print(sum(5,7))

p = lambda x,y:x+y
print(p(5,7))

p2 = lambda x,y,z:x+y+z
print(p2(3,5,7))

# 为什么非得用lambda
# 任何能使用lambda的地方都可以创建一个普通的功能来进行替换.我们将匿名函数用在需要特殊封装的非重用代码上,避免使我们的程序里面充斥着大量的单行函数
# ===================================
# lambda表示匿名函数,如果与之一起使用的pd.series,pd.dataframe,则这一列(表)中的每一个元素都会被输入到lambda函数中,每个元素贯穿lambda中的x,结果会生成一个新的series
# apply()间接的调用函数
# lambda + apply 就是一个薄薄的循环
import pandas as pd
# 例子
df = pd.read_csv('./beijing_tianqi_2018.csv')
print(df.head(5))
# 新加一列'fengmin',显示风力的最小值
df['fengmin'] = df.apply(lambda x:x['fengli'].split('-')[0],axis=1) #让线竖着穿
df['fengmin'] = df['fengli'].apply(lambda x:x.split('-')[0])#apply前面的df或者series,会穿过x,没穿过一条就会去进行一次lambda冒号后边的计算


# 练习:新增一列fengx,这一列只有风向没有风
df['fengx'] = df.apply(lambda x:x['fengxiang'].split('风')[0],axis=1)

# 新增一列month,这一列中显示月
df['month'] = df.apply(lambda x:x['ymd'].split('-')[1],axis=1)
print(df.head(5))
# 新增一列day,这一列显示天
df['day'] = df.apply(lambda x:x['ymd'].split('-')[2],axis=1)
print(df.head(5))
# 法二
df['day'] = df['ymd'].apply(lambda x:x.split('-')[2])
print(df.head(5))