#coding:utf-8
import unittest,time,re,sys
from selenium import webdriver
from config import *
#from except_config import *
from time import *

class TestCase(unittest.TestCase):
    status_tag = {"status": 1}
    def driver_except(self,driver_str, loop_num = 3, sleep_time = 1):
        driver = self.driver
        if self.status_tag["status"] == 1:
            print 'Current Process : ', str(driver_str)
            num = 0
            while num < loop_num:
                try:
                    exec ("retu_temp = " + driver_str)
                except Exception, e:
                    print e
                else:
                    break
                finally:
                    num += 1
                    sleep(sleep_time)
            if num == loop_num:
                self.status_tag["status"] = 0
                return False
            else:
                return retu_temp

    os.makedirs(snapshot_path)
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        print 11
        #self.driver_except('driver.get("http://crm.guxiansheng.cn/")')
        self.driver_except('driver.get("http://www.guxiansheng.cn/")')
        self.verificationErrors = [] #错误的信息将被打印到这个列表中
        self.accept_next_alert = True
        self.driver_except('driver.set_window_size(1440, 900)')


    def isElementExist(self, element):
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    def save_snapshot(self,name):
        self.driver.save_screenshot(snapshot_path + '\\' + name + '_' +  re.sub('[:]', '', str(datetime.datetime.now()).split(' ')[1].split('.')[0]) + '.jpg')
        #print snapshot_path + '\\' + str(name).split('test_')[1] + '_' + re.sub('[:]', '', str(datetime.datetime.now()).split(' ')[1].split('.')[0]) + '.png'
    def is_alert_present(self): #对弹窗异常的处理
         try: self.driver.switch_to_alert()
         except NoAlertPresentException, e: return False
         return True
    def close_alert_and_get_its_text(self): #关闭警告以及对得到文本框的处理
        try:
           alert = self.driver.switch_to_alert()
           alert_text = alert.text
           if self.accept_next_alert:
               alert.accept()
           else:
               alert.dismiss()
           return alert_text
        finally: self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors) #对前面 verificationErrors 方法获得的列表进行比较

    '''
#测试用例1
    def test_login_1(self):
        driver = self.driver
        self.driver_except('driver.find_element_by_name("loginusername").send_keys("18681378808")')
        self.driver_except('driver.find_element_by_name("loginpassword").send_keys("123456")')
        self.driver_except('driver.find_element_by_xpath("//button[@class=\'layui-btn\']").click()')
        flag = TestCase.isElementExist(self, ".//*[@id='app']/div[1]/div/div/div/div/a")
        if flag:
            self.save_snapshot(sys._getframe().f_code.co_name)
            #driver.get_screenshot_as_file("D:\\autotest\\test1.jpg")
            print '登陆成功并截图'.decode('utf-8')
        else:
            print '登录失败'.decode('utf-8')
        #验证是否登录成功
        self.assertTrue(driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/div/div/div/a").get_attribute("class"))
        #进入消息
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[2]/div[1]/ul/li[1]/a").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[2]/div[1]/ul/li[1]/a").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div[2]/div[2]/div[1]/ul/li[3]").click()')
        flag = TestCase.isElementExist(self, ".//*[@id='app']/div[2]/div[2]/div[1]/ul/li[3]")
        if flag:
            self.save_snapshot(sys._getframe().f_code.co_name)
            print '消息查看成功并截图'.decode('utf-8')
        else:
            print '消息截图失败'.decode('utf-8')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/ul/li[1]/a").click()')
        #print driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/h3").get_attribute("header-title")
        self.assertTrue(driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/h3"))

#新增客户
    def test_add(self):
        driver = self.driver
        self.driver_except('driver.find_element_by_name("loginusername").send_keys("18681378808")')
        self.driver_except('driver.find_element_by_name("loginpassword").send_keys("123456")')
        self.driver_except('driver.find_element_by_xpath("//button[@class=\'layui-btn\']").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div[2]/div[2]/div[1]/a/p").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div[2]/div[1]/div/div[2]/a[1]").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/div[2]/div[1]/div/div/input").send_keys("mr.stock")')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/div[2]/div[1]/div/div/input").send_keys("18000000000")')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/div[2]/div[7]/div/div/div[20]/i").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/div[2]/div[8]/div/div/input").send_keys("chennle")')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[2]/div[2]/ul/li[1]").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[4]/button[2]").click()')
    '''
    def test_login(self):
        self.driver_except('driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[2]/a[1]").click()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'loginForm\']/ul/li[1]/input").clear()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'loginForm\']/ul/li[1]/input").send_keys("18081378808")')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'loginForm\']/ul/li[2]/input").clear()')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'loginForm\']/ul/li[2]/input").send_keys("123456")')
        self.driver_except('driver.find_element_by_xpath(".//*[@id=\'loginForm\']/p/input").click()')
        #登录断言
        self.assertTrue(self.driver_except('driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[2]/div/div[1]/a/p")'))

        # 截图
        self.save_snapshot(sys._getframe().f_code.co_name)
        print '登陆成功并截图'.decode('utf-8')
        #self.assertTrue(driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/div/div/div/a").get_attribute("class"))
        #self.assertTrue(driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/div/div/div/a").get_attribute("class"))