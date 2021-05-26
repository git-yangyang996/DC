from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
        self.driver.switch_to.window(search[-1])
        search1 = self.driver.current_window_handle
        time.sleep(3)
        print('点击now line')
        self.driver.find_element_by_xpath(meter.xpath_now_lie).click()

    def test_add_filingjob(self):
        for add_start_minu in range(11,90,11):
            add_end_minu = add_start_minu + 10
            filing_job01_start = '06:' + str(add_start_minu) + ':00'
            filing_job01_end = '06:' + str(add_end_minu) + ':00'

            print('点击add new job')
            time.sleep(4)
            element = WebDriverWait(self.driver,30,1).until(EC.presence_of_element_located((By.XPATH,meter.xpath_new_job)))
            element.click()

            print('title输入')
            self.driver.find_element_by_xpath(meter.xpath_title).send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath(meter.xpath_title).send_keys(Keys.BACK_SPACE)
            self.driver.find_element_by_xpath(meter.xpath_title).send_keys(meter.add_title)

            print('元数据输入')
            self.driver.find_element_by_xpath(meter.xpath_rights).send_keys(meter.add_rights)
            self.driver.find_element_by_xpath(meter.xpath_Origin).send_keys(meter.add_Origin)
            self.driver.find_element_by_xpath(meter.xpath_Source).send_keys(meter.add_Source)
            self.driver.find_element_by_xpath(meter.xpath_comments).send_keys(meter.add_comments)
            self.driver.find_element_by_xpath(meter.xpath_Program_Name).send_keys(meter.add_Program_Name)
            self.driver.find_element_by_xpath(meter.xpath_Category).send_keys(meter.add_Category)
            self.driver.find_element_by_xpath(meter.xpath_Jounalist).send_keys(meter.add_Jounalist)
            self.driver.find_element_by_xpath(meter.xpath_Item_Name).send_keys(meter.add_Item_Name)

            print('选择site')
            self.driver.find_element_by_xpath(meter.xpath_site).click()
            time.sleep(1)
            site_selet = self.driver.find_element_by_xpath(meter.xpath_site_selet_rtmp).click()

            print('channel选择')
            self.driver.find_element_by_xpath(meter.xpath_channel_clik).click()
            self.driver.find_element_by_xpath(meter.xpath_channel_select_rtmp01).click()

            print('signal输入')
            self.driver.find_element_by_xpath(meter.xpath_signal_list).click()
            self.driver.find_element_by_xpath(meter.xpath_signal_select_pal).click()

            #任务任务日期输入
            self.driver.find_element_by_xpath(meter.xpath_start_data).send_keys(Keys.CONTROL,'a')
            self.driver.find_element_by_xpath(meter.xpath_start_data).send_keys(Keys.SEPARATOR)
            self.driver.find_element_by_xpath(meter.xpath_start_data).send_keys('2021-04-01')

            self.driver.find_element_by_xpath(meter.xpath_end_data).send_keys(Keys.CONTROL, 'a')
            self.driver.find_element_by_xpath(meter.xpath_end_data).send_keys(Keys.SEPARATOR)
            self.driver.find_element_by_xpath(meter.xpath_end_data).send_keys('2021-04-01')
            self.driver.find_element_by_xpath(meter.xpath_end_data).send_keys(Keys.ENTER)

            time.sleep(2)
            print('任务时间输入')
            # 保持焦点情况下输入
            self.driver.find_element_by_xpath(meter.xpath_start_time).click()
            self.driver.switch_to.active_element.send_keys(filing_job01_start)
            # 保持焦点情况下输入
            self.driver.find_element_by_xpath(meter.xpath_end_time).click()
            self.driver.switch_to.active_element.send_keys(filing_job01_end)

            print('创建任务')
            self.driver.find_element_by_xpath(meter.xpath_filingjob_confrom).click()
