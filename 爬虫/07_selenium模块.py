#! /usr/bin/env python
# -*- coding: utf-8 -*-
# selenium 模块
'''
什么是selenium模块:基于浏览器的自动化模块
selenium测试直接运行在浏览器里面,就像真的用户在操作一样
这个模块的功能主要包括:
    1.测试浏览器的兼容性
    2.测试系统性能
使用程序:
    1.安装selenium模块
    2.下载浏览器驱动程序
    下载链接:
    https://chromedriver.storage.googleapis.com/index.html
103.0.5060.114
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from lxml import etree
# 实例化浏览器
# s = Service('./chromedriver.exe')
driver = webdriver.Chrome()
# 让实例化的浏览器对指定url发起请求
driver.get('http://www.baidu.com')
# 两秒后切换到京东
sleep(2)
driver.get('http://www.jd.com')
# 获取京东的网页源码数据
data = driver.page_source
# 将源码数据转换成html文件
result = etree.HTML(data)
print(result)
# 再过两秒退出浏览器
sleep(2)
driver.quit()
