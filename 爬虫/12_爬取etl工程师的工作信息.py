#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-aotomation'])
s=Service('./chromedriver.exe')
driver = webdriver.Chrome(options=option)
driver.get('http://www.51job.com')
# 定位到搜索框,并输入etl工程师
searchinput = driver.find_element(By.XPATH,'//*[@id="kwdselectid"]')
searchinput.send_keys('ETL工程师')
sleep(3)
button = driver.find_element(By.XPATH,'html/body/div[3]/div/div[1]/div/button')
# 点击搜索按钮
button.click()
sleep(10)
# 解析网页
#  查找一个元素可以用find_element 和find_elements
# 查找多个元素只能用find_elements
list = driver.find_element(By.XPATH,'html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div')
for result in list:
    work = result.text.split('\n')
    print(work)

sleep(10)
driver.quit()
