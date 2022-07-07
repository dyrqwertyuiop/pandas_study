#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
'''
网络请求有两个模块:
1.urllib:古老,麻烦
2.requests:好
作用:模拟浏览器对网站发起请求
流程要遵循下面的步骤:
    1.指定url :网址
    2.发起网络请求
    3.获取数据
    4.存储数据
'''
# 指定url
url='http://www.baidu.com'
# 发起网络请求
response=requests.get(url=url)
# 查看相应的状态码
# 常见的状态码 200:服务器成功返回网页 404:网页不存在 503:服务不可用
print(response.status_code)
# 查看请求的url
print(response.url)
# 查看网页的头部信息:承载了关于客户端浏览器,请求页面,服务器等相关信息
print(response.headers)
# 以文本的形式打印网页源代码
# print(response.text)
# 获取网页数据
# 以字节流的形式打印网页源代码(获取网页数据)
# 什么是字节流:直接从网上抓取数据,没有经过任何处理,没有经过任何编码,是一个bytes类型,我们在硬盘以及网络上传输的字符串都是bytes类型pr
print(response.content)
# 打印cookies信息
'''
cookies是一种能让网站把少量的数据存储到客户端或内存,当你浏览某个网站的时候,由服务器置于你硬盘上一个非常小的文件就是cookies,他可以记录你的用户id,密码,或者你浏览过的网页,以及停留的时间,当你再次来到这个网站的时候,网站就会通过读取你的cookies得知你的相关信息,就可以做出相应的动作,比如不让你输入用户ID和密码就能直接登录,或者直接显示欢迎你

本质上说,cookies可以看作你的身份证,但是不会被当做代码去执行,也不会传病毒,一个网站只能取得它放在你电脑中的cookies,无法从其他的cookies中获取信息
'''
print(response.cookies)
