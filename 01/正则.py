#! /usr/bin/env python
# -*- coding: utf-8 -*-

#python中的正则re
import re
# re.match() 从字符串的开始位置进行匹配,匹配成功会返回一个匹配到的对象,使用该对象的group功能得到匹配成功的字符串
# result = re.match('abc','abcffahfwaeiabcasldjfaoabcdsajabc')
# print(result)
# #abc
# print(result.group())

# 2.re.search() 扫描整个字符串返回第一个匹配成功的对象
# result = re.search('ab+c','asjoeabbbcdsjoao')
# print(result.group())

# 3.re.findall() 在字符串中找到所有满足正则表达式的字符串,并返回一个列表,如果没有就会得到一个空列表
# result = re.findall('[a-z]','asjofeaoaabbcsdjfoaofapaabbbcajfoaoabc')
# print(result)

# 4.re.sub()
# sub(要替换的字符串,替换为什么字符串,测试字符串,替换次数,(忽略大小写,这个参数默认为零))
# result = re.sub('a','冰冰','binge is a good man haha',4)
# print(result)

# 贪婪匹配和懒惰匹配
str1 = 'bingeisagoodmanveryshuaisjdfjo'
# 懒惰匹配:匹配尽可能少的字符
print(re.findall('b.*?e',str1))
# 贪婪匹配:匹配尽可能多的字符
print(re.findall('b.*',str1))

