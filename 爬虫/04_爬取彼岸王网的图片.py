#! /usr/bin/env python
# -*- coding: utf-8 -*-
# url='https://pic.netbian.com/4kyouxi/index_2.html'
import requests
from lxml import etree
'''
使用lxml模块可以处理html文件,还可以用于web的爬取,这个模块在解析大型文档时速度特别快,并且提供了简单的转换方法将数据转换成python中的数据类型
'''
for page in range(2,6):
    url = 'https://pic.netbian.com/4kyouxi/index_%s.html'%page
    response = requests.get(url)
    # print(response)
    # etree.HTML()用来解析字符串格式(Bytes)的html文档对象
    root=etree.HTML(response.content)
    # 使用Xpath来对标签进行解析,获取最终目标(XPATH简单理解为在html文档中检索匹配的工具)
    #获取图片链接//:全局 @:表示引用
    img_src_list=root.xpath('//div[@class="slist"]/ul/li/a/img/@src')
    # print(img_src_list)
    # 获取图片名称
    img_name_list=root.xpath('//div[@class="slist"]/ul/li/a/img/@alt')
    # print(img_name_list)
    for src,name in zip(img_src_list,img_name_list):
        #拼接完整的图片地址
        src = 'http://pic.netbian.com' + src
        img_response = requests.get(src)
        #保存图片
        file = open(name+'.jpg','wb')
        file.write(img_response.content)
        file.close()
