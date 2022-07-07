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
    response = requests.get(url)
    # print(response)