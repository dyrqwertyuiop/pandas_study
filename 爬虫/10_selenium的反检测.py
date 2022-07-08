#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 我们用selenium爬取网站的时候,会有特征值,网站会将特征值检测出来,可能有的网站登录是就会报错10001:请求参数异常
#所以我们可以修改登录信息
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
# selenium中有一个反检测模块
from selenium.webdriver import ChromeOptions
# 实例化ChromeOptions
option = ChromeOptions()
# print(option)
# 以键值对形式加入参数
option.add_experimental_option('excludeSwithes',['enable-automation'])
# =================上面就是反检测的代码,不用记,不用背,拿来直接用
# 实例化浏览器
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(chrome_options=option)
# 让实例化的浏览器对指定url发起请求
driver.get('http://www.baidu.com')
sleep(5)
driver.quit()
