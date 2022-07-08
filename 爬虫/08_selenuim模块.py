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
driver.get('http://www.taobao.com')
# 在淘宝搜索框中输入ipad并搜索
# 标签定位find_element:查找一个元素并返回该元素对象,当页面有多个元素对象返回第一个
# 找到淘宝中的搜索框find_element(属性,值)
search_input = driver.find_element('id','q')
# 往搜索框里面输入IPAD
search_input.send_keys('ipad')
sleep(3)
# 点击搜索按钮
button = driver.find_element(By.CLASS_NAME,'btn-search')
button.click()

sleep(20)
driver.quit()
