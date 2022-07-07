#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
#一对一关系
left = pd.DataFrame({'id':[11,12,13,14],'name':['小红花','小航','小斌','小明'],'score':['3','4','5','6']})
print(left)
right = pd.DataFrame({'id':[11,12,13,14],'age':['16','80','72','95'],'score':['3','4','5','6']})
print(right)
right_left = pd.merge(left,right,on='id',suffixes=('_hang','_bin')) #默认_x,_y
print(right_left)

#一对多
left1 = pd.DataFrame({'id':[11,12,13,14],'name':['小红','小明','小刚','小辉']})
right1 = pd.DataFrame({'id':[11,11,11,12,12,12,13,13,13,14,14,14],'score':['语文88','数学78','英语72','语文88','数学78','英语72','语文88','数学78','英语72','语文88','数学78','英语72']})
print(left1)
print(right1)
l1r1 = pd.merge(left1,right1,on = 'id')
print (l1r1)