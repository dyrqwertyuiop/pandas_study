#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
# selenium中有一个反检测模块
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
# 实例化ChromeOptions
option = ChromeOptions()
# print(option)
# 以键值对形式加入参数
option.add_experimental_option('excludeSwitches',['enable-aotomation'])
# =================上面就是反检测的代码,不用记,不用背,拿来直接用
# 实例化浏览器
s = Service('./chromedriver.exe')
driver = webdriver.Chrome()
# 让实例化的浏览器对指定url发起请求
driver.get('http://www.jd.com')
# 定位搜索框输入键盘
# //*:选择html中所有元素,无论名称是什么
#
searchInput=driver.find_element(By.XPATH,'//*[@id="key"]')
searchInput.send_keys('手机')
# 定位到搜索框并搜索
button=driver.find_element(By.XPATH,'//*[@id="search"]/div/div[2]/button/i')
button.click()
sleep(5)

'''
模拟页面下拉
滚动页面函数:execute_script()  execute执行 script脚本
滚动到页面底部:document:文件 
window.scrollTo(0 ,document.body.scrollHeight)
滚动到页面顶部
window.scrollTo(0,0)
'''

# 三秒后将页面下拉到底部
sleep(3)
driver.execute_script('window.scrollTo(0 ,document.body.scrollHeight)')
# # 五秒后将页面拉到顶部
# sleep(5)
# driver.execute_script('window.scrollTo(0,0)')

# 3秒之后翻页
sleep(3)
pagebutton = driver.find_element(By.XPATH,'//*[@id="J_bottomPage"]/span[1]/a[9]')
pagebutton.click()
sleep(5)
driver.quit()


















