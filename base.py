#!/usr/bin/env/python
# coding = utf-8

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from page.login import login

import time,os

def get_ele_times(driver, times, func):

    try:

        return WebDriverWait(driver, times).until(func)

    except Exception as msg:

        print(msg)

def open_browser():

    # 打开浏览器

    os.system('taskkill -f -im chromedriver.exe')

    driver = webdriver.Chrome()

    driver.maximize_window()

    return driver

def open_url(driver, url):

    # 打开测试网址

    driver.get(url)

def again_login(driver, login_acc, login_pwd):

    js = "var q = document.documentElement.scrollTop=0"

    driver.execute_script(js)

    time.sleep(0.5)

    driver.find_element_by_xpath('//span[text()="退出登录"]/..').click()

    time.sleep(2)

    driver.find_element_by_xpath('//div[@class="ant-modal-confirm-btns"]/button[2]').click()

    time.sleep(1.5)

    driver.find_element_by_xpath('//div[@class="login-box"]/button').click()

    time.sleep(2)

    login_acc_ele = driver.find_element_by_xpath('//*[@id="_umname"]')

    login_pwd_ele = driver.find_element_by_xpath('//*[@id="test"]')

    login_acc_ele.clear()

    login_acc_ele.send_keys(login_acc)

    login_pwd_ele.clear()

    login_pwd_ele.send_keys(login_pwd)

    driver.find_element_by_xpath('//*[@id="submit"]/span').click()

def is_element_exist(driver, element):

    # 判断元素是否存在，若存在，返回True，不存在返回False

    flag = True

    time.sleep(1)

    try:

        driver.find_element_by_xpath(element)

        return flag

    except:

        flag = False

        return flag

def in_element_text(driver,element, comment):

    try:

        t = driver.find_element_by_xpath(element).text

        if comment in t:

            return True

        else:

            return False

    except:

        return False

if __name__ == '__main__':

    driver = open_browser()

    login(driver=driver, login_acc='zhanghu', login_pwd='mima1234')

    # driver.quit()
