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


class Test_toolbal_setting(object):
    @pytest.mark.flaky(reruns = 1)
    def setup_class(self):
        Page_module.Mail.login_chrome(self)
        Page_module.Mail.login_web_ingest(self)

    '''点击listmode'''
    def test_01(self):
        Page_module.Mail.toolbal_listmode(self)


