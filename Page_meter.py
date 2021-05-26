from selenium import webdriver
from datetime import datetime,timedelta

class web_UI(object):

    # 获取系统时间
    ostime = datetime.now()
    time = ostime.strftime('%Y-%m-%d %H:%M:%S')
    time_date = ostime.strftime('%Y-%m-%d')
    time_date_d = ostime.strftime('%d')
    # 设置任务开始时间和结束时间
    minu01 = 5
    minu02 = minu01 + 5
    ostime_start = (ostime + timedelta(minutes=minu01)).strftime('%H:%M:%S')
    ostime_end = (ostime + timedelta(minutes=minu02)).strftime('%H:%M:%S')
    #设置任务等待时间
    sleep_time_start = minu01 * 60 + 20
    sleep_time_durtion = (minu02 - minu01)*60 + 20
    # 设置需要修改后的时间
    ostime_modify_start = (ostime + timedelta(minutes=3)).strftime('%H:%M:%S')
    ostime_modify_end = (ostime + timedelta(minutes=8)).strftime('%H:%M:%S')

    # 设置周期任务日期
    day = 5#设置任务周期时间
    ostime_start_data = ostime.strftime('%Y-%m-%d')
    ostime_end_data = (ostime + timedelta(days=day)).strftime('%Y-%m-%d')


    #访问地址
    cm_url = "https://srf.test.com/CMWeb/login.aspx?aspxerrorpath=/"

    #cm登录
    cm_xpath_login = "login-button"
    xpath_web_ingest_login ='/html/body/div[2]/div[5]/div[7]/div[1]/input[4]'

    # 多语言列表
    language_list = ["0Ky është vetëm një test i cil i ka veçoritë e veta! Shpresoj se do të jetë në rregull ",
                     "Možeš li doći da pogledaš ovaj džak",
                     "Ο Ταγίπ Ερντογάν δήλωσε «Ο αγωγός είναι ένα σημαντικό βήμα για τις σχέσεις των δύο χωρών» Από την πλευρά του",
                     "Rami ya ɓurme Kare ‘yancin ɗan Adam Yaran makaranta na ƙoƙari ‘Yancin mata",
                     "Presiden Joko Widodo menegaskan: “Rakyat harus tetap tenang!” ",
                     "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoópqrsśtuwyzźż",
                     "KYWÇÃÕÂÊÔÁÉÍÓÚÀABCDEFGHIJKLMNOPQRSTUVWXYZkywçãõâêôáéíóúàabcdefghijklmnopqrstuvwxyz",
                     "ÁÃÂÀÇÉÊÍÓÔÕÚABCDEFGHIJKLMNOPQRSTUVWXYZáãâàçéêíóôõúabcdefghijklmnopqrstuvwxyz",
                     "KYWÇÃÕÂÊÔÁÉÍÓÚÀABCDEFGHIJKLMNOPQRSTUVWXYZkywçãõâêôáéíóúàabcdefghijklmnopqrstuvwxyz",
                     "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZaăâbcdefghiîjklmn,o,pqrsștțuvwxyz",
                     "ABVGDĐEŽZIJKLLJMNNJOPRSTĆUFHCČDŽŠabvgdđežzijklljmnnjoprstćufhcčdžš",
                     "ËëžešžšÇçαβγδεζηθικλμνξοπσςτυφχψωΓΔΘΙΛΞΟΠΡΣΦΨΩYyƁƊɓɗƙŁĆĘłŃńóśźżüÃÕÂÊÔÁÉÍÓÚÀãõâêôáéíóúàäşğdžšĐđć",
                     "web ingest rtmp hd50 1080i",
                     'ΦΨΩYyŁĆĘłŃńóśźżüÃÕÂÊÔÁÉÍÓÚÀãõâêôáéíóúàäşğdžšĐđćΡΣ',
                     ]

    # 字符类型
    character_list = ['1234567890',
                      'qwertyuiopasdfghjklzxcvbnm',
                      'QWERTYUIOPASDFGHJKLZXCVBNM',
                      '~!#$%()_+{}`-=[];\', ',
                      '1234567890 ',
                      "200字符ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUV"
                      "WXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRST"
                      "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef00000014"
                      ]

    # 格式遍历数据
    format_PAL_list = ['PAL 1080I HD50 24bit', 'PAL 1080I HD35 24bit', 'PAL 1080I HD25 24bit', 'PAL 1080I HD25 16bit',
                       'PAL 1080I EX35 24bit', 'PAL 720p HD50 24bit',
                       'PAL 720p HD35 24bit']
    fromat_N_list = ['NTSC 1080I HD50 24bit', 'NTSC 1080I HD35 24bit', 'NTSC 1080I HD25 24bit', 'NTSC 1080I HD25 16bit',
                     'NTSC 1080I EX35 24bit', 'NTSC 720p HD35 24bit', 'NTSC 720p HD50 24bit']

    # 用户名，密码
    use_list = ['srf.com\yangyang', 'test-yy', 'yy6', 'yy1', 'yangyang']
    pwd_list = ['Sobey123', 'yy', 'S210gdbaX1!']

    #赋值
    add_language = language_list[0]
    add_character = character_list[0]
    add_fromat = fromat_N_list[4]
    add_modify = character_list[1]
    # sso登录
    add_use_SSO = use_list[4]
    add_pwd_SSO = pwd_list[2]
    # 普通登录
    add_use = use_list[3]
    add_pwd = pwd_list[1]

    # 输入参数
    filing_job_meta_list = ['title', 'Rights', 'Comments', 'Program Name', 'Category', 'Jounalist', 'Item Name']
    add_title = add_fromat
    add_rights = add_fromat
    add_Origin = add_fromat
    add_Source = add_fromat
    add_comments = add_fromat
    add_Program_Name = add_fromat
    add_Category = add_fromat
    add_Jounalist = add_fromat
    add_Item_Name = add_fromat
    add_url_send = 'rtmp://10.0.100.218:1935/live/'
    add_url_send_50p = 'rtmp://10.0.100.218:1936/live/'

    '''界面UI元素定位'''

    # 快速采集参数设置：
    # channel_modify = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[2]'
    # channel_modify_title = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[1]/form/div[1]/div/input'
    # channel_modify_signal = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[1]/form/div[2]/div/span/div[2]/input'
    # channel_modify_save = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[1]/div[3]/div[2]/i[1]'
    # channel_quick = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div[' + str(channel) + ']/div[2]/button'
    channel_quick_Origin = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/form/div/div[1]/div/textarea'
    channel_quick_Source = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/form/div/div[2]/div/input'
    channel_quick_comfort = '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/div/button[1]'

    # 工具栏路径
    xpath_Expand_or_Retract = '//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/i[1]'
    xpath_new_job = '//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/i[2]'
    title_new_job = "[title ='Add New Task']"
    xpath_now_lie = '//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/i[3]'
    xpath_channel_mode = '//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/i[4]'
    xpath_list_mode = '//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/i[5]'
    xpath_datelist = '//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/div/input'
    xpath_use_out = '//*[@id="app"]/div/header/div/div/i[1]'
    xpath_use_setting = '//*[@id="app"]/div/header/div/div/i[2]'
    xpath_help = '//*[@id="app"]/div/header/div/div/i[3]'
    xpath_help_confrom = '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/div/button[1]'

    # setting窗口内功能路径
    xpath_use_setting_xpath = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div/div[4]/div/span[3]'
    xpath_use_setting_date = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/form/div/div/label[1]/span[1]'
    xpath_use_setting_weekdat = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/form/div/div/label[2]/span[1]'
    xpath_use_setting_confrom = '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/div/button[1]'
    xpath_use_setting_clos = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/button/i'
    xpath_use_setting_cancel = '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/div/button[2]'

    # fliling job内元数据路径
    xpath_title = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[1]/div/input'
    xpath_rights = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[2]/div/textarea'
    xpath_comments = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[3]/div/textarea'
    xpath_Program_Name = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[4]/div/input'
    xpath_Category = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[5]/div/input'
    xpath_Jounalist = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[6]/div/input'
    xpath_Item_Name = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[7]/div/input'
    xpath_channel_clik = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[2]/div/div/div/input'
    xpath_end_time_date = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[4]/div/span/div[2]/input'
    xpath_Material = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[3]'
    xpath_Material_date = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/label[1]/span[1]'
    xpath_Material_weekday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/label[2]/span[1]'
    xpath_site = "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[9]/div[1]/div/div/div[1]/input"
    xpath_site_selet_rtmp = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
    xpath_Duration = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[9]/div[3]/div/div/div/span[3]'
    xpath_Duration_time = '11'
    xpath_start_time = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[9]/div[1]/div/div/div[2]/input'
    xpath_end_time = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[9]/div[2]/div/div/div[2]/input'
    xpath_Task_Type = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div/div/div/div[1]/input'
    xpath_Task_Type_Scheduled_Recording = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
    xpath_start_data = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[1]/div/div/div[1]/input'
    xpath_end_data = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[2]/div/div/div[1]/input'

    # filing job内channel路径
    channel_01 = 7
    channel_02 = channel_01 + 1
    channel_03 = channel_01 + 2
    channel_04 = channel_01 + 3
    xpath_channel_select_rtmp01 = "/html/body/div[3]/div[1]/div[1]/ul/li[" + str(channel_01) + "]"
    xpath_channel_select_rtmp02 = '/html/body/div[3]/div[1]/div[1]/ul/li[' + str(channel_02) + ']'
    xpath_channel_select_rtmp03 = '/html/body/div[3]/div[1]/div[1]/ul/li[' + str(channel_03) + ']'
    xpath_channel_select_rtmp04 = '/html/body/div[3]/div[1]/div[1]/ul/li[' + str(channel_04) + ']'
    xpath_channel_select_test = '/html/body/div[3]/div[1]/div[1]/ul/li[13]'

    # filing job内功能按钮定位
    xpath_filingjob_confrom = '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/div/button[1]'
    xpath_filingjob_cancel = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/button[2]'

    # 周期任务类型
    xpath_type_list = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div/div/div/div[1]/input'
    xpath_type_Manual_Start = '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span'
    xpath_Periodic = '/html/body/div[7]/div[1]/div[1]/ul/li[2]'
    xpath_Periodic_weekly = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[1]/div/div/label[2]/span[2]'
    xpath_Periodic_monthly = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[1]/div/div/label[3]'
    xpath_Periodic_weekly_Monday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[1]/label/span[2]'
    xpath_Periodic_weekly_Tuesday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[2]/label/span[2]'
    xpath_Periodic_weekly_Wednesday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[3]/label/span[2]'
    xpath_Periodic_weekly_Thursday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[4]/label/span[2]'
    xpath_Periodic_weekly_Friday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[5]/label/span[2]'
    xpath_Periodic_weekly_Saturday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[6]/label/span[2]'
    xpath_Periodic_weekly_Sunday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[7]/label/span[2]'
    xpath_Periodic_monthly_02 = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[2]/label/span[1]/span'
    xpath_Periodic_monthly_03 = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div/div[3]/label/span[1]/span'
    xpath_Periodic_noenddate = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div[3]/label'
    xpath_Periodic_daily_end_by = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div[2]/div/input'
    xpath_Periodic_daily_star_by = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[2]/div[1]/div/input'
    xpath_Periodic_weekly_star_by = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[3]/div[1]/div/input'
    xpath_Periodic_weekly_end_by = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[10]/div[3]/form/div[3]/div[2]/div/input'
    xpath_Periodic_monthly_list = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[11]/div[3]/form/div[2]'

    # channel扩展页面内功能路径
    xpath_channel_rtmp01_modify = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/i'
    xpath_channel_rtmp02_modify = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[11]/div[1]/div[3]/div[2]/i'
    xpath_channel_modify_name1 = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[10]/div[1]/div[3]/div[1]/form/div[1]/div/input'
    xpath_channel_modify_name2 = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[11]/div[1]/div[3]/div[1]/form/div[1]/div/input'
    xpath_channel_modify_signal_list = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[10]/div[1]/div[3]/div[1]/form/div[2]/div/span/div/input'
    xpath_channel_modify_save = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[10]/div[1]/div[3]/div[2]/i[1]'
    xpath_channel_modify_cancel = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[10]/div[1]/div[3]/div[2]/i[3]'
    xpath_channel_quick = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[10]/div[2]/button'

    # signal路径
    xpath_channel_modify_signal_50i = '/html/body/div[2]/div[1]/div/div[3]'
    xpath_url_cust = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[4]/div/label/span[1]/span'
    xpath_url_xpath = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[3]/div/input'
    xpath_signal_select_pal = '/html/body/div[5]/div[1]/div/div[2]'  # 位数为下拉框内的signal顺序
    xpath_signal_select_n = '/html/body/div[4]/div[1]/div/div[1]'
    xpath_signal_select_rtmp50i = '/html/body/div[4]/div[1]/div/div[2]'
    xpath_signal_select_rtmp50p = '/html/body/div[4]/div[1]/div/div[3]'
    xpath_signal_list = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[4]/div/span/div/input'
    xpath_start_signal_list = '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[4]/div/div/input'
    xpath_filingjob_signal_meter = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/form/div[8]/div[4]/div/span/div[2]/input'

    # material页面路径参数
    xpath_material_tab = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[3]'
    xpath_material_Destination_date = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/label[1]/span[1]/span'
    xpath_material_Destination_date_select = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/label[1]/span[@class="el-checkbox__input is-checked"]'
    xpath_material_Destination_weekday = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/label[2]/span[1]/span'
    xpath_material_Destination_weekday_select = '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/label[2]/span[@class="el-checkbox__input is-checked"]'
    xpath_material_tab_confrim = '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/div/button[1]'

    # 时间线相关路径
    # channel task父节点定位信息
    Channel_Rtmp01_task = '/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[3]'
    Channel_Rtmp02_task = '/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[19]/div[3]/div'

    Channel_Rtmp01_tast = '/html/body/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[12]/div[3]/div'
    Channel_Rtmp04_task = '/html/body/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[13]/div[3]/div'

    # # 定位时间线上内的任务位置
    # time_line_Rtmp01_task = '/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[' + task_sums + ']'
    # time_line_Rtmp02_task = '/html/body/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[3]/div[3]/div/div[' + task_sums + ']'

    # 定位任务检索数据
    Channel_task_class = '[class="task-item h100 tal bc-4f bd-76 abs box-b clearfix"]'

    '''时间线任务右键菜单路径'''
    # 未开始采集任务右键菜单定位
    time_line_right_delt = '//*[@id="app"]/div/div[1]/div[3]/ul/li[1]'
    time_line_right_property = '/html/body/div/div/div[1]/div[3]/ul/li[2]'
    delete_comfrim = '/html/body/div[2]/div/div[3]/button[2]'

    # 开始采集右键菜单定位
    time_line_right_start_property = '/html/body/div[1]/div/div[1]/div[3]/ul/li[4]'

    # 采集完任务右键菜单等位
    time_line_right_complete_property = '//*[@id="app"]/div/div[1]/div[3]/ul/li[3]'

    # 用户退出二级弹框
    xpath_use_out_ok = "/html/body/div[3]/div/div[3]/button[2]"
    xpath_use_out_cancel = "/html/body/div[3]/div/div[3]/button[1]"

    # list mode检查元素
    element_listmode_siganltype = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[2]'
    element_listmode_tsekname = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[3]'
    listmode_lie = []
    for list in range(2, 10):
        list = str(list)
        element_listmode_siganltype = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[' + list + ']'
        listmode_lie.append(element_listmode_siganltype)

    listmode_lie01 = listmode_lie

    listmode_txt_list = ['//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[5]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[6]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[7]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[8]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[9]/span[3]',
                         '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[1]/div/div[10]/span[3]'
                         ]

    # 元数据判断
    def Judgment(a, b):

        for meta in filing_job_meta_list:

            if a == b:
                print(meta, 'ok')
            else:
                print(meta, '元数据与创建时输入的元数据不符')

    # 元数据判断方法二：
    def Judgment_02(a, b):
        differ = set(a.items()) ^ set(b.items())
        print('以下元素值不相等：', differ)

    # xpath获取value值
    def def_xpath_value(self, a):
        self.driver.find_element_by_xpath(a).get_attribute('value')

    # 获取channel内任务个数
    def channel_task(self, channel_id):
        task_sum = self.driver.find_element_by_xpath(channel_id)  # channel定位
        task_sums = len(task_sum.find_elements_by_css_selector(Channel_task_class))
        task_sums = str(task_sums)
        time_line_Rtmp_task = '//*[@id="app"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[12]/div[3]/div/div[' + task_sums + ']'

    # 循环批量采集任务时间配置
    time_start = '08:25:00'
    time_end = '12:25:00'

    add_start_minu = 0
    add_end_minu = add_start_minu + 5
    filing_job01_start = '04:0' + str(add_start_minu) + ':00'
    filing_job01_end = '04:0' + str(add_end_minu) + ':00'

    # add_channel_name = 'rtmp-hd50 1080i quck ingest'
    # add_across_the_day_start = '23:50:55'
    # add_across_the_day_end = '00:30:55'
    # add_periodic_star = '2021-04-06'
    # add_periodic_end = '2021-04-10'
    # add_end_time_date = time_date


























