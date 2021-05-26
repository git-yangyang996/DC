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

    def test_quickingest(self):
        #循环任务创建通道输入
        self.driver.implicitly_wait(60)
        for channel in range(107, 200):

            #print('创建同一时间的计划任务')
            #print('点击add new job')
            new_job = self.driver.find_element_by_xpath(meter.xpath_new_job)
            self.driver.execute_script("arguments[0].click();", new_job)

            #print('title输入')
            self.driver.find_element_by_xpath(meter.xpath_title).clear()
            self.driver.find_element_by_xpath(meter.xpath_title).send_keys(meter.add_title)
            #其余元素据输入
            self.driver.find_element_by_xpath(meter.xpath_rights).send_keys(meter.add_rights)
            self.driver.find_element_by_xpath(meter.xpath_Origin).send_keys(meter.add_Origin)
            self.driver.find_element_by_xpath(meter.xpath_Source).send_keys(meter.add_Source)
            self.driver.find_element_by_xpath(meter.xpath_comments).send_keys(meter.add_comments)
            self.driver.find_element_by_xpath(meter.xpath_Program_Name).send_keys(meter.add_Program_Name)
            self.driver.find_element_by_xpath(meter.xpath_Category).send_keys(meter.add_Category)
            self.driver.find_element_by_xpath(meter.xpath_Jounalist).send_keys(meter.add_Jounalist)
            self.driver.find_element_by_xpath(meter.xpath_Item_Name).send_keys(meter.add_Item_Name)

            if isElementExist.xpath_panduan(self,self.driver.find_element_by_xpath(meter.xpath_site)):

                self.driver.find_element_by_xpath(meter.xpath_site).click()
            else:

                self.driver.find_element_by_xpath(meter.xpath_site).click()
            #site输入
            site_selet = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[4]')
            self.driver.execute_script("arguments[0].click();", site_selet)
            #channel选择
            self.driver.find_element_by_xpath(meter.xpath_channel_clik).click()

            if isElementExist.xpath_panduan(self,self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li['+str(channel)+']')):

                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li['+str(channel)+']'))
            else:

                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[' + str(channel) + ']'))


            self.driver.find_element_by_xpath(meter.xpath_signal_list).click()
            signal = WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[1]/div/div[2]')))
            signal.click()

            # 保持焦点情况下输入
            self.driver.find_element_by_xpath(meter.xpath_start_time).click()
            self.driver.switch_to.active_element.send_keys(meter.time_start)#开始时间

            # 保持焦点情况下输入
            self.driver.find_element_by_xpath(meter.xpath_end_time).click()
            self.driver.switch_to.active_element.send_keys(meter.time_end)#结束时间

            self.driver.find_element_by_xpath(meter.xpath_filingjob_confrom).click()
            time.sleep(4)



            print('通道' + str(channel) + '创建任务')

if __name__ == '__mian__':
    pytest.main()

