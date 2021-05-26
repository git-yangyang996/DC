from selenium import webdriver
import allure
import time
import pytest
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('E:\python\cloud V194-web ingest\GIT LAB')
import Page_isElementExist
import Page_meter
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
        self.driver.implicitly_wait(60)
        print("cm login")
        self.driver.find_element_by_id("userName").send_keys(meter.add_use)
        self.driver.find_element_by_id("pwd").send_keys(meter.add_pwd)
        self.driver.find_element_by_id("login-button").click()


        # print('SSO登录')
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://mbh.sobeycloud.net/CM/#/login")
        # self.driver.maximize_window()
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys(meter.add_use_SSO)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[2]/input').send_keys(meter.add_pwd_SSO)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/input[3]').click()

        # # 登录
        print("web ingest login")
        self.driver.find_element_by_xpath(meter.xpath_web_ingest_login).click()
        search = self.driver.window_handles
        self.driver.switch_to.window(search[-1])
        print('点击now line')
        self.driver.find_element_by_xpath(meter.xpath_now_lie).click()

    def test_stop_job(self):
        self.driver.implicitly_wait(60)
        for channel in range(104, 200):
            property_task=self.driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div["+str(channel)+"]/div["
                                                                                                                                                            "3]/div["
                                                                                                                                                         "1]/div[1]")
            ActionChains(self.driver).context_click(property_task).perform()
            self.driver.find_element_by_xpath(meter.time_line_right_delt).click()
            print('stop:',channel)