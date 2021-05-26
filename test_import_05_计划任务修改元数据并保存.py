from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import Page_isElementExist
import Page_meter
import Page_module
from selenium.webdriver import ActionChains
import os
import pytest


class Test_login_case(object):

    def setup_class(self):

        '''打开浏览器'''
        Page_module.Mail.login_chrome(self)

        '''登录web ingest'''
        Page_module.Mail.login_web_ingest(self)


    def test_01(self):
        self.driver.implicitly_wait(30)
        '''点击add new jobsssss'''
        Page_module.Mail.webingest_new_filingjob(self)

        '''输入元数据'''
        Page_module.Mail.webingest_filingjob_inputelement(self)

        '''任务创建'''
        Page_module.Mail.filingjob_confrom(self)

        '''时间线上任务定位'''
        Page_module.Mail.nowline_job(self)

        '''打开任务属性窗口'''
        Page_module.Mail.nowline_job_property(self)

        '''修改任务元数据'''
        Page_module.Mail.webingest_flilngjob_modify(self)

        '''取修改后的值'''
        Page_module.Mail.filingjob_value(self)

        '''修改保存'''
        Page_module.Mail.filingjob_confrom(self)

    '''任务未开始读取并检查元数据'''
    def test_02(self):
        '''时间线上任务定位'''
        Page_module.Mail.nowline_job(self)

        '''打开任务属性窗口'''
        Page_module.Mail.nowline_job_property(self)

        '''未开始任务取值'''
        Page_module.Mail.filingjob_meter(self)

        '''任务数据校验'''
        Page_module.Mail.filingjob_batch_click(self)


    """采集中的任务读取并检查元数据"""
    def test_03(self):

        '''等待任务开始'''
        time.sleep(Page_meter.web_UI.sleep_time_start)

        '''时间线上任务定位'''
        Page_module.Mail.nowline_job(self)

        '''打开任务属性窗口'''
        Page_module.Mail.start_nowline_job_property(self)

        '''任务采集中取值'''
        Page_module.Mail.filingjob_meter(self)

        '''任务数据校验'''
        Page_module.Mail.filingjob_start_batch_click(self)



    """采集完的任务读取并检查元数据"""
    def test_04(self):
        '''等待任务结束'''
        time.sleep(Page_meter.web_UI.sleep_time_durtion)

        '''时间线上任务定位'''
        Page_module.Mail.nowline_job(self)

        '''打开任务属性窗口'''
        Page_module.Mail.end_nowline_job_property(self)

        '''任务采集完成后取值'''
        Page_module.Mail.filingjob_meter(self)

        '''任务数据校验'''
        Page_module.Mail.filingjob_start_batch_click(self)



    if __name__ == '__main__':
        pytest.main([r'--alluredir=E:\python\workspace\cloud_webingest\target\allure-results', '--clean-alluredir'])
