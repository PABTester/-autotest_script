#!/usr/bin/env/python

# coding = utf-8

import time



from selenium_test.base import Base



class TestWindows(Base):

    def test_window(self):

        self.driver.get("https://www.baidu.com/")

        self.driver.find_element_by_link_text('登录').click()

        print(self.driver.current_window_handle)



    # 点击立即注册

        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()

    print(self.driver.current_window_handle)

    print(self.driver.window_handles)



    windows =self.driver.window_handles

    self.driver.switch_to.window(windows[-1])



    self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')

    self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('13000000000')



    self.driver.switch_to.window(windows[0])

    self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()



    self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('login_username')

    self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('login_password')

    self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()


    time.sleep(3)
