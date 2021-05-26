from selenium import webdriver
import allure
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
sys.path.append('E:\python\cloud V194-web ingest\GIT LAB')
import meter
import isElementExist
@allure.feature('元数据类型输入，创建任务')
# print('元数据类型输入，创建任务')
class Test_fillingjob(object):
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

    @allure.title('点击new job输入元数据创建任务')
    def test_01_meter_character(self):

        for character in meter.character_list:
            print('点击add new job')
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_xpath(meter.xpath_new_job).click()
            print("-完成")

            print('title输入')
            self.driver.find_element_by_xpath(meter.xpath_title).send_keys(character)
            print("-完成")

            print('rights输入')
            self.driver.find_element_by_xpath(meter.xpath_rights).send_keys(character)
            print("-完成")

            print('comments输入')
            self.driver.find_element_by_xpath(meter.xpath_comments).send_keys(character)
            print("-完成")

            print('Program Name输入')
            self.driver.find_element_by_xpath(meter.xpath_Program_Name).send_keys(character)
            print("-完成")

            print('Category输入')
            self.driver.find_element_by_xpath(meter.xpath_Category).send_keys(character)
            print("-完成")

            print('Jounalist输入')
            self.driver.find_element_by_xpath(meter.xpath_Jounalist).send_keys(character)
            print("-完成")

            print('Item Name输入')
            self.driver.find_element_by_xpath(meter.xpath_Item_Name).send_keys(character)
            print("-完成")

            print('signal选择')
            self.driver.find_element_by_xpath(meter.xpath_url_cust).click()
            self.driver.find_element_by_xpath(meter.xpath_url_xpath).send_keys(meter.add_url_send)

            print("计划任务创建")
            self.driver.find_element_by_xpath(meter.xpath_confrom).click()
            time.sleep(15)

            self.driver.quit()

if __name__ == '__main__':
    print('测试完成')
