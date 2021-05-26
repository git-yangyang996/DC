import Page_meter
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import Page_isElementExist

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



class Mail:
    '''初始化'''
    def __init__(self,driver):
        self.driver = driver

    '''打开浏览器'''
    def login_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Page_meter.web_UI.cm_url)
        self.driver.maximize_window()

    '''非sso登录webingest'''
    def login_web_ingest(self):# web ingest登录封装
        #非sso登录cm login
        self.driver.implicitly_wait(30)
        page_web.by_id(self,"userName").send_keys(Page_meter.web_UI.add_use)
        page_web.by_id(self,"pwd").send_keys(Page_meter.web_UI.add_pwd)
        page_web.by_id(self,Page_meter.web_UI.cm_xpath_login).click()
        time.sleep(3)
        # print("web ingest login")
        page_web.by_xpath(self,Page_meter.web_UI.xpath_web_ingest_login).click()

        #tab页面切换
        search = self.driver.window_handles
        self.driver.switch_to.window(search[-1])
        search1 = self.driver.current_window_handle
        print(search1)
        #点击居中
        page_web.by_xpath(self, Page_meter.web_UI.xpath_now_lie).click()

    '''sso模式下登录webingest'''
    def SSO_login_web_ingest(self):

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys(
            Page_meter.web_UI.add_use_SSO)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[2]/input').send_keys(
            Page_meter.web_UI.add_pwd_SSO)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/input[3]').click()

        #web ingest登录
        self.driver.find_element_by_xph(Page_meter.web_UI.xpath_web_ingest_login).click()
        search = self.driver.window_handles
        '''点击居中'''
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_now_lie).click()
        self.driver.switch_to.window(search[-1])
        search1 = self.driver.current_window_handle
        print(search1)

    """打开new job"""
    def webingest_new_filingjob(self):
        time.sleep(5)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_new_job).click()

    '''filingjob内输入元数据'''
    '''输入'''
    def webingest_filingjob_inputelement(self):
        '''元数据输入'''
        page_web.by_xpath(self,Page_meter.web_UI.xpath_title).clear()
        page_web.by_xpath(self,Page_meter.web_UI.xpath_title).send_keys(Page_meter.web_UI.add_title)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_rights).send_keys(Page_meter.web_UI.add_rights)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_comments).send_keys(Page_meter.web_UI.add_comments)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Program_Name).send_keys(Page_meter.web_UI.add_Program_Name)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Category).send_keys(Page_meter.web_UI.add_Category)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Jounalist).send_keys(Page_meter.web_UI.add_Jounalist)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Item_Name).send_keys(Page_meter.web_UI.add_Item_Name)

        '''channel选择'''
        page_web.by_xpath(self,Page_meter.web_UI.xpath_channel_clik).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_channel_select_rtmp02).click()

        '''signal选择'''
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_signal_list).click()
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_signal_select_n).click()

        '''输入任务开始时间'''
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_start_time).clear()
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_start_time).send_keys(Page_meter.web_UI.ostime_start)
        # 保持焦点情况下输入
        #self.driver.switch_to.active_element.send_keys(Page_meter.web_UI.ostime_start)

        '''输入任务结束时间'''
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_end_time).clear()
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_end_time).send_keys(Page_meter.web_UI.ostime_end)
        # 保持焦点情况下输入
        #self.driver.switch_to.active_element.send_keys(Page_meter.web_UI.ostime_end)
        time.sleep(3)
    '''修改'''
    def webingest_flilngjob_modify(self):
        '''元数据输入'''
        page_web.by_xpath(self, Page_meter.web_UI.xpath_title).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_title).send_keys(Page_meter.web_UI.add_modify)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_rights).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_rights).send_keys(Page_meter.web_UI.add_modify)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_comments).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_comments).send_keys(Page_meter.web_UI.add_modify)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Program_Name).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Program_Name).send_keys(Page_meter.web_UI.add_modify)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Category).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Category).send_keys(Page_meter.web_UI.add_modify)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Jounalist).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Jounalist).send_keys(Page_meter.web_UI.add_modify)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Item_Name).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Item_Name).send_keys(Page_meter.web_UI.add_modify)

        # '''channel选择'''
        # page_web.by_xpath(self, Page_meter.web_UI.xpath_channel_clik).click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_channel_select_rtmp02).click()
        #
        # '''signal选择'''
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_signal_list).click()
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_signal_select_n).click()
        #
        # '''输入任务开始时间'''
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_start_time).clear()
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_start_time).send_keys(Page_meter.web_UI.ostime_start)
        # # 保持焦点情况下输入
        # # self.driver.switch_to.active_element.send_keys(Page_meter.web_UI.ostime_start)
        #
        # '''输入任务结束时间'''
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_end_time).clear()
        # self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_end_time).send_keys(Page_meter.web_UI.ostime_end)
        # # 保持焦点情况下输入
        # # self.driver.switch_to.active_element.send_keys(Page_meter.web_UI.ostime_end)

    '''任务类型选择'''
    '''daily'''
    def filingjob_select_daily_tasktype(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_type_list).click()
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Periodic).click()

        """选择创建日期"""
        '''开始'''
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Periodic_daily_star_by).clear()
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Periodic_daily_star_by).send_keys(Page_meter.web_UI.ostime_start_data)
        '''结束'''
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Periodic_daily_end_by).clear()
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Periodic_daily_end_by).send_keys(Page_meter.web_UI.ostime_end_data)
    '''month'''
    def filingjob_select_month_tasktype(self):
        """创建monthly周期任务"""
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_type_list).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Periodic).click()
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Periodic_monthly).click()

        print('点击选择创建日期')
        monthly_list = range(1, 32)
        for daily in monthly_list:
            daily = str(daily)
            print("勾选日期" + daily + "号")
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[' + daily + ']').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div'
                                              '[' + str(Page_meter.web_UI.time_date_d) + ']').click()
    '''weekly'''
    def filingjob_select_weekly_tasktype(self):

        """创建weekly周期任务"""
        page_web.by_xpath(self,Page_meter.web_UI.xpath_type_list).click()
        self.driver.implicitly_wait(30)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Periodic).click()
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Periodic_weekly).click()

        """勾选日期"""
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Friday).click()
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Monday).click()
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Saturday).click()
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Sunday).click()
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Thursday).click()
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Tuesday).click()
        # self.driver.find_element_by_xpath(meter.xpath_Periodic_weekly_Wednesday).click()


    '''取值'''
    '''创建时filing job内取值'''
    def filingjob_value(self):
        '''设置全局变量'''
        global data_filingjob_channel, data_filingjob_signal, data_filingjob_end_time, data_filingjob_tasktype, data_filingjob_start_time
        #取channel值
        data_filingjob_channel = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_channel_clik).get_attribute('value')
        #取signal值
        data_filingjob_signal = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_signal_list).get_attribute('value')
        #取输入的开始时间
        data_filingjob_start_time = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_start_time).get_attribute('value')
        #取结输入的束时间
        data_filingjob_end_time = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_end_time).get_attribute('value')
        #取任务类型
        data_filingjob_tasktype = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Task_Type).get_attribute('value')
    '''任务创建后元数据取值'''
    def filingjob_meter(self):
        '''设置全局变量'''
        global data_title, data_rights, data_Comments, data_Program_Name, data_Category, data_Jounalist, data_Item_Name, \
            data_channel_filingjob, data_siganl, data_start_time, data_end_time, data_Task_Type,start_data_signal
        '''数据取值'''
        data_title = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_title).get_attribute('value')
        data_rights = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_rights).get_attribute('value')
        #notstart_data_Origin = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Origin).get_attribute('value')
        #notstart_data_Source = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Source).get_attribute('value')
        data_Comments = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_comments).get_attribute('value')
        data_Program_Name = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Program_Name).get_attribute("value")
        data_Category = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Category).get_attribute('value')
        data_Jounalist = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Jounalist).get_attribute('value')
        data_Item_Name = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Item_Name).get_attribute('value')
        data_channel_filingjob = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_channel_clik).get_attribute('value')

        '''判断signal路径取值'''
        if Page_isElementExist.web_panduan.xpath_panduan(self,Page_meter.web_UI.xpath_signal_list):

            data_siganl = self.driver.find_element_by_xpath(
                Page_meter.web_UI.xpath_signal_list).get_attribute('value')

        else:
            start_data_signal = self.driver.find_element_by_xpath(
                Page_meter.web_UI.xpath_start_signal_list).get_attribute('value')


        #print('未开始采集任务的signal值为：', notstart_data_siganl)
        #print('取开始结束时间')
        data_start_time = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_start_time).get_attribute('value')
        data_end_time = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_end_time).get_attribute('value')
        data_Task_Type = self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_Task_Type).get_attribute('value')
        #print('未开始采集任务的Task Type值为：', notstart_data_Task_Type)
        '''关闭filing job窗口'''
        time.sleep(1)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_filingjob_cancel).click()


    '''任务创建'''
    def filingjob_confrom(self):
        page_web.by_xpath(self,Page_meter.web_UI.xpath_filingjob_confrom).click()
    """filing job窗口关闭"""
    def filingjob_cannel(self):
        page_web.by_xpath(self,Page_meter.web_UI.xpath_filingjob_cancel).click()

    '''时间线上任务定位'''
    def nowline_job(self):
        '''设置全局变量'''
        global task_sums, time_line_Rtmp01_task, time_line_Rtmp02_task
        time.sleep(3)
        #获取channel内任务个数
        task_sum = self.driver.find_element_by_xpath(Page_meter.web_UI.Channel_Rtmp02_task)  # channel定位
        task_sums = len(task_sum.find_elements_by_css_selector(Page_meter.web_UI.Channel_task_class))
        task_sums = str(task_sums)
        # 定位时间线上内的任务位置
        time_line_Rtmp01_task = '/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[18]/div[3]/div/div[' + task_sums + ']'
        time_line_Rtmp02_task = '/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[19]/div[3]/div/div[' + task_sums + ']'

    '''右键属性'''
    '''未开始任务右键属性'''
    def nowline_job_property(self):
        time.sleep(3)
        #print('需要检查的任务定位')
        property_task = self.driver.find_element_by_xpath(time_line_Rtmp02_task)
        print(property_task)
        #print('打开任务右键菜单')
        ActionChains(self.driver).context_click(property_task).perform()

        #print('打开任务属性页')
        self.driver.find_element_by_xpath(Page_meter.web_UI.time_line_right_property).click()
    '''采集中任务右键属性'''
    def start_nowline_job_property(self):
        time.sleep(3)
        # print('需要检查的任务定位')
        property_task = self.driver.find_element_by_xpath(time_line_Rtmp02_task)
        print(property_task)
        # print('打开任务右键菜单')
        ActionChains(self.driver).context_click(property_task).perform()

        '''打开属性'''
        self.driver.find_element_by_xpath(Page_meter.web_UI.time_line_right_start_property).click()
    '''采集完任务右键属性'''
    def end_nowline_job_property(self):
        time.sleep(1)
        # print('需要检查的任务定位')
        property_task = self.driver.find_element_by_xpath(time_line_Rtmp02_task)
        print(property_task)
        # print('打开任务右键菜单')
        ActionChains(self.driver).context_click(property_task).perform()
        time.sleep(1)
        '''打开属性'''
        self.driver.find_element_by_xpath(Page_meter.web_UI.time_line_right_complete_property).click()


    '''filing job内校验元数据'''
    '''元数据单独输入比较'''
    def filingjob_click(self):

        """创建任务时输入的元数据"""
        add_data_list = {'title': Page_meter.web_UI.add_title, 'comments': Page_meter.web_UI.add_comments,
                             'rights': Page_meter.web_UI.add_rights, 'Program_Name': Page_meter.web_UI.add_Program_Name,
                             'Category': Page_meter.web_UI.add_Category, 'Jounalist': Page_meter.web_UI.add_Jounalist,
                             'Item_Name': Page_meter.web_UI.add_Item_Name, 'channel': data_filingjob_channel ,
                             'signal': data_filingjob_signal, 'start_time': data_filingjob_start_time,
                             'end_time': data_filingjob_end_time, 'tasktype': data_filingjob_tasktype,
                             }
        """创建任务后取出来的元数据"""
        data_list = {'title': data_title, 'comments': data_Comments,
                         'rights': data_rights, 'Program_Name': data_Program_Name,
                         'Category': data_Category, 'Jounalist': data_Jounalist,
                         'Item_Name': data_Item_Name, 'channel': data_channel_filingjob,
                         'signal': data_siganl, 'start_time': data_start_time,
                         'end_time': data_end_time, 'tasktype': data_Task_Type,
                         }
        print('输入：',add_data_list)
        print('创建后取出',data_list)
        print('未开始采集元数据比较：', Page_meter.web_UI.Judgment_02(data_list, add_data_list))
        assert Page_meter.web_UI.add_title in data_title
    '''创建任务后元数据批量输入比较'''
    def filingjob_batch_click(self):
        """创建任务时输入的元数据"""
        add_data_list = {'title': Page_meter.web_UI.add_modify, 'comments': Page_meter.web_UI.add_modify,
                         'rights': Page_meter.web_UI.add_modify, 'Program_Name': Page_meter.web_UI.add_modify,
                         'Category': Page_meter.web_UI.add_modify, 'Jounalist': Page_meter.web_UI.add_modify,
                         'Item_Name': Page_meter.web_UI.add_modify, 'channel': data_filingjob_channel,
                         'signal': data_filingjob_signal, 'start_time': data_filingjob_start_time,
                         'end_time': data_filingjob_end_time, 'tasktype': data_filingjob_tasktype,
                         }
        """创建任务后取出来的元数据"""
        data_list = {'title': data_title, 'comments': data_Comments,
                     'rights': data_rights, 'Program_Name': data_Program_Name,
                     'Category': data_Category, 'Jounalist': data_Jounalist,
                     'Item_Name': data_Item_Name, 'channel': data_channel_filingjob,
                     'signal': data_siganl, 'start_time': data_start_time,
                     'end_time': data_end_time, 'tasktype': data_Task_Type,
                     }
        print('输入：', add_data_list)
        print('创建后取出', data_list)
        print('未开始采集元数据比较：', Page_meter.web_UI.Judgment_02(data_list, add_data_list))
        #assert Page_meter.web_UI.add_title in data_title
    '''任务开始采集后的元数据比较'''
    def filingjob_start_click(self):
        # 创建任务时输入的元数据
        add_data_list = {'title': Page_meter.web_UI.add_title, 'comments': Page_meter.web_UI.add_comments,
                         'rights': Page_meter.web_UI.add_rights, 'Program_Name': Page_meter.web_UI.add_Program_Name,
                         'Category': Page_meter.web_UI.add_Category, 'Jounalist': Page_meter.web_UI.add_Jounalist,
                         'Item_Name': Page_meter.web_UI.add_Item_Name, 'channel': data_filingjob_channel,
                         'signal': data_filingjob_signal, 'start_time': data_filingjob_start_time,
                         'end_time': data_filingjob_end_time, 'tasktype': data_filingjob_tasktype,
                         }
        # 创建任务后取出来的元数据
        data_list = {'title': data_title, 'comments': data_Comments,
                     'rights': data_rights, 'Program_Name': data_Program_Name,
                     'Category': data_Category, 'Jounalist': data_Jounalist,
                     'Item_Name': data_Item_Name, 'channel': data_channel_filingjob,
                     'signal': start_data_signal, 'start_time': data_start_time,
                     'end_time': data_end_time, 'tasktype': data_Task_Type,
                     }
        print('输入：', add_data_list)
        print('创建后取出', data_list)
        print('未开始采集元数据比较：', Page_meter.web_UI.Judgment_02(data_list, add_data_list))
        assert Page_meter.web_UI.add_title in data_title
    '''任务开始采集后，元数据批量比较'''
    def filingjob_start_batch_click(self):
        # 创建任务时输入的元数据
        add_data_list = {'title': Page_meter.web_UI.add_modify, 'comments': Page_meter.web_UI.add_modify,
                         'rights': Page_meter.web_UI.add_modify, 'Program_Name': Page_meter.web_UI.add_modify,
                         'Category': Page_meter.web_UI.add_modify, 'Jounalist': Page_meter.web_UI.add_modify,
                         'Item_Name': Page_meter.web_UI.add_modify, 'channel': data_filingjob_channel,
                         'signal': data_filingjob_signal, 'start_time': data_filingjob_start_time,
                         'end_time': data_filingjob_end_time, 'tasktype': data_filingjob_tasktype,
                         }
        # 创建任务后取出来的元数据
        data_list = {'title': data_title, 'comments': data_Comments,
                     'rights': data_rights, 'Program_Name': data_Program_Name,
                     'Category': data_Category, 'Jounalist': data_Jounalist,
                     'Item_Name': data_Item_Name, 'channel': data_channel_filingjob,
                     'signal': start_data_signal, 'start_time': data_start_time,
                     'end_time': data_end_time, 'tasktype': data_Task_Type,
                     }
        print('输入：', add_data_list)
        print('创建后取出', data_list)
        print('未开始采集元数据比较：', Page_meter.web_UI.Judgment_02(data_list, add_data_list))
        #assert Page_meter.web_UI.add_title in data_title


    """工具栏"""
    """Ssetting"""
    '"打开setting界面"'
    def toolbal_setting(self):
        page_web.by_xpath(self,Page_meter.web_UI.xpath_use_setting).click()
    """点击x关闭setting窗口"""
    def toolbal_setting_clos(self):
        print('点击右上角关闭键')
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_use_setting_clos).click()
        if Page_isElementExist.web_panduan.xpath_panduan(self,Page_meter.web_UI.xpath_use_setting_clos):
            print('窗口已关闭')
        else:
            print('error:窗口未关闭')
            assert False
    """点击cancle关闭setting窗口"""
    def toolbal_setting_cancel(self):
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_use_setting_cancel).click()
        time.sleep(1)
        assert Page_isElementExist.web_panduan.xpath_panduan(self, Page_meter.web_UI.xpath_use_setting_cancel)
    '''设置路径为daily'''
    def toolbal_setting_date(self):
        clas = page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_date).get_attribute("class")
        # print(clas01)
        if clas == 'el-checkbox__input is-checked':
            print('已勾选')
            assert False
        else:
            page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_date).click()
            page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_confrom).click()
            page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting).click()
            clas = page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_date).get_attribute("class")
            if clas == 'el-checkbox__input is-checked':
                print('setting内正确勾选')
                Mail.toolbal_setting_cancel(self)
            else:
                print('没有正确勾选')
                assert False

        Mail.webingest_new_filingjob(self)
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Material).click()
        filngjob_cls = page_web.by_xpath(self,Page_meter.web_UI.xpath_Material_date).get_attribute("class")
        if filngjob_cls == 'el-checkbox__input is-checked':
            print('filing job内勾选显示正确')
            Mail.filingjob_cannel(self)
        else:
            print('未显示勾选')
            assert False
    '''设置路径为weekly'''
    def toolbal_setting_weekly(self):
        clas = page_web.by_xpath(self,Page_meter.web_UI.xpath_use_setting_weekdat).get_attribute("class")
        #print(clas01)
        if clas == 'el-checkbox__input is-checked':
            print('已勾选')
            assert False
        else:
            page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_weekdat).click()
            page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_confrom).click()
            page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting).click()
            clas = page_web.by_xpath(self, Page_meter.web_UI.xpath_use_setting_weekdat).get_attribute("class")
            if clas == 'el-checkbox__input is-checked':
                print('setting内正确勾选')
                Mail.toolbal_setting_cancel(self)
            else:
                print('没有正确勾选')
                assert False

        Mail.webingest_new_filingjob(self)
        page_web.by_xpath(self, Page_meter.web_UI.xpath_Material).click()
        filngjob_cls = page_web.by_xpath(self, Page_meter.web_UI.xpath_Material_date).get_attribute("class")
        if filngjob_cls == 'el-checkbox__input is-checked':
            print('filing job内勾选显示正确')
            Mail.filingjob_cannel(self)
        else:
            print('未显示勾选')
            assert False


    '''设置路劲'''
    def toolbal_setting_xpath(self):

        """浏览器侧边滚动条"""
        #js = "var q=document.documentElement.scrollTop=10000"

        '''定位到指定元素下'''
        # target = self.driver.find_element_by_xpath('//*[@id="2"]/div/div[3]/p[1]')
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)

        '''div下滚动条置顶'''
        js = 'document.getElementsByClassName("scrollbar-container folder-container")[0].scrollTop=0'
        time.sleep(1)
        self.driver.execute_script(js)

        '''查找元素'''
        xpath = self.driver.find_element_by_css_selector('[title = "Ingest"]')
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", xpath)

        # 将滚动条移动到页面的顶部
        # js = "var q=document.documentElement.scrollTop=0"
        # time.sleep(2)






    """工具栏内点击expand"""
    def toolbal_expand(self):
        print('点击expand')
        page_web.by_xpath(self,Page_meter.web_UI.xpath_Expand_or_Retract).click()
        assert Page_isElementExist.web_panduan.xpath_panduan(self,Page_meter.web_UI.xpath_channel_rtmp01_modify)
    """工具栏内点击listmode"""
    def toolbal_listmode(self):
        self.driver.find_element_by_xpath(Page_meter.web_UI.xpath_list_mode).click()
        time.sleep(1)
        print('taskname元素判断')
        for xpath in Page_meter.web_UI.listmode_txt_list:
            list_panduan = Page_isElementExist.web_panduan.xpath_panduan(self, xpath)
            if list_panduan:
                print('列路径正确')
                assert True
            else:
                print('ERROR:未定位到列')
                assert False