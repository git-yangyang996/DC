from selenium import webdriver
import allure
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append('E:\python\cloud V194-web ingest\GIT LAB')
import meter
import isElementExist

allure.description('tollbal点击')
class Test_expand(object):
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


    def test_tool(self):

        print('点击now line')
        self.driver.find_element_by_xpath(meter.xpath_now_lie).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(meter.xpath_now_lie).click()
        time.sleep(5)

        print('Expand or Retract')
        self.driver.find_element_by_xpath(meter.xpath_Expand_or_Retract).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(meter.xpath_Expand_or_Retract).click()
        time.sleep(5)

        print('list mode')
        self.driver.find_element_by_xpath(meter.xpath_list_mode).click()
        time.sleep(3)
        print('taskname元素判断')
        for xpath in meter.listmode_lie01:
            list_panduan = isElementExist.xpath_panduan(self,xpath)
            if list_panduan:
                assert True
                print('列路径正确')
            else:
                assert False
                print('未定位到列')
        time.sleep(5)

        print('channel mode')
        self.driver.find_element_by_xpath(meter.xpath_channel_mode).click()
        time.sleep(5)

        print('日期窗口')
        self.driver.find_element_by_xpath(meter.xpath_datelist).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(meter.xpath_datelist).click()

        print('use setting')
        self.driver.find_element_by_xpath(meter.xpath_use_setting).click()
        self.driver.find_element_by_xpath(meter.xpath_use_setting_xpath).click()
        self.driver.find_element_by_xpath(meter.xpath_use_setting_date).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(meter.xpath_use_setting_weekdat).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(meter.xpath_use_setting_confrom).click()

        print('help窗口')
        self.driver.find_element_by_xpath(meter.xpath_help).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(meter.xpath_help_confrom).click()

        print('web ingest用户登出')
        self.driver.find_element_by_xpath(meter.xpath_use_out).click()

        self.driver.quit()

if __name__ == '__main__':
    print('测试完成')





