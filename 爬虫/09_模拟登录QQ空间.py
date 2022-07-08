#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from lxml import etree
from selenium.webdriver.common.by import By

# 实例化浏览器
# s = Service('./chromedriver.exe')
driver = webdriver.Chrome()
# 让实例化的浏览器对指定url发起请求
driver.get('http://qzone.qq.com')
# iframe作用域:包含另一个html文档的框架
driver.switch_to.frame('login_frame')
# 定位到账号密码登录
login_button = driver.find_element('id','switcher_plogin')
# 点击按钮
login_button.click()
# 两秒后输入账号和密码
sleep(2)
QQ = driver.find_element('id','u')
QQ.send_keys('3482353261')
pwd = driver.find_element('id','p')
pwd.send_keys('d15947619835')
# 点击登录按钮
button = driver.find_element('id','login-button')
button.click()
sleep(2)
driver.quit()