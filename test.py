from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
# sys.path.append('C:\Users\administrator.SRF\Desktop\SRG -web ingest\GIT LAB')
import Page_isElementExist
import Page_meter
import Page_module
from selenium.webdriver import ActionChains
import os
import pytest

#使用；"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\chrome"

'''接管以打开的网页进行调试'''
class Test_case(object):
    def test_01(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(chrome_options = self.chrome_options)


        Page_module.Mail.nowline_job(self)
        Page_module.Mail.nowline_job_property(self)