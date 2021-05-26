from selenium import webdriver
import Page_meter

class page_web():
    def __init__(self,driver):
        self.driver = driver

    '''基础定位封装'''
    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    def by_name(self,name_):
        return self.driver.find_element_by_name(name_)

    def by_css(self,css_):
        return self.driver.find_element_by_css_selector(css_)

    def by_xpath(self,xpath_):
        return self.driver.find_element_by_xpath(xpath_)


