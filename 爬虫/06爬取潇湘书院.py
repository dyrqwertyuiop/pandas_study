#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from lxml import etree
"""
https://www.xxsy.net/search?&s_type=4&sort=9&pn=1
https://www.xxsy.net/search?&s_type=4&sort=9&pn=2
https://www.xxsy.net/search?&s_type=4&sort=9&pn=3
我想得到前五页的小说名称，作者姓名，小说类型，更新时间，获取字数
%s:字符串占位符
%d:整数占位符
%f:浮点数占位符
"""
for page in range(1,6):
    url='https://www.xxsy.net/search?&s_type=4&sort=9&pn=%d'%page
    # print(url)
    # 设定请求头:告诉服务器关于客户端环境请求正文相关的一些信息,如浏览器版本,请求参数长度
    headers = {'User_agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
    response = requests.get(url,headers)
    # print(response)
    # 转换成html标签
    root = etree.HTML(response.content)
    # print(root)
    novels=root.xpath('//div[@class="result-list"]/ul/li')
    # print(novels)
    x =0
    for novel in novels:
        # 获取小说名称
        # 注意我们获取的是全部小说名称,而不是小说名称列表,因为我们通过xpath解析结果是列表,所以我们应该在解析结果后面加上列表来得到小说名称
        name=novel.xpath('//div[@class="info"]/h4/a/text()')[x] #text()标签里的文本
        # print(name)
        #获取作者姓名
        author = novel.xpath('//div[@class="info"]/h4/span/a[1]/text()')[x]
        # print(author)
        #获取小说类型
        type1 = novel.xpath('//div[@class="info"]/h4/span/a[2]/text()')[x]
        # print(type1)
        #获取更新时间
        time = novel.xpath('//div[@class="info"]/p[2]/span[1]/text()')[x]
        # print(time)
        # 获取字数
        num = novel.xpath('//div[@class="info"]/p[2]/span[2]/text()')[x]
        # print(num)
        # print(name,author,type1,time,num,'\n')
        x = x + 1
        #把爬取的数据写入一个csv文件
        f = open('小说信息.csv','a',encoding='gbk')
        if x==1 and page == 1:
            f.write('小说名称,作者姓名,小说类型,更新时间,字数')
            f.write('\n')
        f.write(name+','+author+','+type1+','+time+','+num)
        f.write('\n')
        f.close()

