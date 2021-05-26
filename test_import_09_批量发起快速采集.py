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


print("批量发起计划采集任务")
class Test_login_case(object):

    @allure.title('登录web ingest')
    def setup_class(self):
        print('非sso登录')
        self.driver = webdriver.Chrome()
        self.driver.get("https://mbh.sobeycloud.net/CM/#/login")
        self.driver.maximize_window()
        print("cm login")
        self.driver.find_element_by_id("userName").send_keys(meter.add_use)
        self.driver.find_element_by_id("pwd").send_keys(meter.add_pwd)
        self.driver.find_element_by_id("login-button").click()
        time.sleep(5)

        # print('SSO登录')
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://mbh.sobeycloud.net/CM/#/login")
        # self.driver.maximize_window()
        # # 登录
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys(meter.add_use_SSO)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[2]/input').send_keys(meter.add_pwd_SSO)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/input[3]').click()

        print("web ingest login")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(meter.xpath_web_ingest_login).click()
        time.sleep(3)
        search = self.driver.window_handles
        self.driver.switch_to.window(search[-1])
        time.sleep(3)
        print('点击now line')
        self.driver.find_element_by_xpath(meter.xpath_now_lie).click()

    def test_quickingest(self):
        # 循环任务创建通道输入
        for channel in range(2, 102):
            time.sleep(3)
            self.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div["+str(channel)+"]/div[2]/button["
                                                                                                                                              "1]").click()
            self.driver.find_element_by_css_selector("[class ~= 'textarea-input']").send_keys('rtmp')
            self.driver.find_element_by_xpath(meter.channel_quick_Source).send_keys('rtmp')
            self.driver.find_element_by_xpath(meter.channel_quick_comfort).click()

