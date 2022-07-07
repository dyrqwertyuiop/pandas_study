#! /usr/bin/env python
# -*- coding: utf-8 -*-

# merge:作用是在pandas中通过merge将不同的表按照相同的列关联在一个表里
# 语法:pd.merge(left,right,how,on,suffiexs)
# left:要关联的df/series对
# right:要关联的df/series对象
# how:关联的类型left right inner outer
# on:关联的类型left ,right必须有相同的列
# suffiexs:关联后要是还有相同的列名,自动添加关联前的表名作为列名的前缀
import pandas as pd
import numpy as np
users = pd.read_csv('./movieslens-1m/users.dat',engine='python',sep='::',header=None,names=['UserID','Genres','Age','Occupation','Zip-code'])
# print(users.head(5))
ratings = pd.read_csv(r'./movieslens-1m/ratings.dat',engine='python',sep='::',header=None,names=['UserID','MovieID','Rating','Timestamp'])
# print(ratings.head(5))
movies = pd.read_csv('./movieslens-1m/movies.dat',engine='python',sep='::',header=None,encoding='ISO-8859-1',names=['MovieID','Title','Genres'])
# print(movies.head(5))

# user_rating = pd.merge(users,ratings,on = 'UserID',how = 'outer')
# print(user_rating)

# rating_movie = pd.merge(ratings,movies,on='MovieID',how='outer')
# print(rating_movie)

user_movie = pd.merge(users,movies,on='Genres',how='outer')
print(user_movie)