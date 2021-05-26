from selenium import webdriver
import allure
import time
import pytest
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('E:\python\cloud V194-web ingest\GIT LAB')
import isElementExist
import meter
from selenium.webdriver import ActionChains
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



print("批量发起快速采集任务")
class Test_login_case(object):

    @allure.title('登录web ingest')
    def setup_class(self):
        print('非sso登录')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://mbh.sobeycloud.net/CM/#/login")
        self.driver.maximize_window()
        print("cm login")
        self.driver.find_element_by_id("userName").send_keys(meter.add_use)
        self.driver.find_element_by_id("pwd").send_keys(meter.add_pwd)
        self.driver.find_element_by_id("login-button").click()
        time.sleep(5)

        # print('ADFS登录')
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        # self.driver.get("https://srf.test.com/CMWeb/login.aspx")
        # self.driver.maximize_window()

        # # 登录
        # self.driver.find_element_by_xpath('//*[@id="idp_OtherRpPanel"]/label[1]').click()
        # self.driver.find_element_by_xpath('//*[@id="idp_RelyingPartyDropDownList"]').click()
        # self.driver.find_element_by_xpath('//*[@id="idp_RelyingPartyDropDownList"]/option[2]').click()
        # self.driver.find_element_by_xpath('//*[@id="idp_SignInButton"]').click()
        # self.driver.find_element_by_id('userName').send_keys(meter.add_use)
        # self.driver.find_element_by_id("pwd").send_keys(meter.add_pwd)
        # self.driver.find_element_by_id("login-button").click()
        # time.sleep(10)

        print("web ingest login")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(meter.xpath_web_ingest_login).click()
        time.sleep(3)
        search = self.driver.window_handles
        print(search)
        self.driver.switch_to.window(search[-1])
        search1 = self.driver.current_window_handle
        print(search1)
        time.sleep(3)
        print('点击now line')
        self.driver.find_element_by_xpath(meter.xpath_now_lie).click()

    def test_quickingest(self):
        for channel in range(2, 102):
            self.driver.implicitly_wait(60)
            time.sleep(3)
            print('点击modify')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[2]').click()

            print('title定位')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[1]/form/div[1]/div/input').send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[1]/form/div[1]/div/input').send_keys(Keys.BACK_SPACE)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[1]/form/div[1]/div/input').send_keys(meter.add_channel_name)

            print('点击signal')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[1]/form/div[2]/div/span/div[2]/input').click()
            self.driver.implicitly_wait(30)

            print('signal选择')
            # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]').click()
            self.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)

            print('save')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[2]/i[1]').click()
            self.driver.implicitly_wait(30)

            print('发起快速采集任务')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[2]/button').click()

            print('输入必填项')
            self.driver.find_element_by_xpath(meter.channel_quick_Origin).send_keys('1')
            self.driver.find_element_by_xpath(meter.channel_quick_Source).send_keys('1')
            self.driver.find_element_by_xpath(meter.channel_quick_comfort).click()
            self.driver.implicitly_wait(20)
            # time.sleep(6)
            print('通道' + str(channel) + '创建任务')

if __name__ == '__mian__':
    pytest.main()

