from selenium.common.exceptions import NoSuchElementException

class web_panduan():
    def xpath_panduan(self, xpath):
        flag = True
        try:
            self.driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag

    def link_panduan(self, txt):
        flag = True
        try:
            self.driver.find_element_by_link_text(txt)
            return flag
        except:
            flag = False
            return flag

    def class_name_panduan(self, selector):
        flag = True
        try:
            self.driver.find_elements_by_class_name(selector)
            return flag
        except:
            flag = False

    # def xpath_selected(self,xpath):
    #     try:
    #         self.driver.find_element_by_xpath(xpath).is_selected()
    #         return flag
    #     except:
    #         flag = False




