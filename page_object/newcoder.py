from selenium.webdriver.common.by import By

from base.base_page import BasePage

from selenium import webdriver

import common.global_var
import  time
import json
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver import ChromeOptions
class testnowcoder(BasePage):
    def login_newcoder(self):
        self.driver = webdriver.Chrome()
        self.open("https://www.nowcoder.com/exam/company")
        common.global_var.set_value("gdriver", self.driver)

        time.sleep(5)
        self.getcookie()


    def getcookie(self):
        with open("../data/mycookie.txt", "w+") as f:
            f.write(json.dumps(self.driver.get_cookies()))
            common.global_var.set_value("gcookie", self.driver.get_cookies())


    def openother(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=option)
      #  self.driver = webdriver.Chrome()
        self.open("https://www.nowcoder.com/exam/company")
        # common.global_var.set_value("gdriver", self.driver)
        # self.driver.delete_all_cookies()
        # with open("../data/mycookie.txt", "r+") as f:
        #     cookies = json.loads(f.read())
        #     for cookie in cookies:
        #
        #         self.driver.add_cookie(cookie)
        #
        #
        # self.refresh()
        # time.sleep(3)

        self.performvip()


    def performvip(self):


        self.vip = {By.XPATH, '//*[@id="jsApp"]/header/header/nav/div[2]/div[3]'}
        # ele = self.locator(self.vip)
        # time.sleep(3)
        # ActionChains(self.driver).move_to_element(ele).perform()

       # self.click(self.vip)
        self.mouseperform(self.vip)


    def openbaidu(self):
        self.driver = webdriver.Chrome()
        self.open("https://www.baidu.com/")
        time.sleep(2)
        #self.shezhi = {By.LINK_TEXT,"设置"}

       # ele = self.locator(self.shezhi)
       # print(ele)
       # ActionChains(self.driver).move_to_element(ele).perform()

        # 定位到要悬停的元素

        # 对定位到的元素执行鼠标悬停操作

        above = self.driver.find_element_by_link_text("设置")
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(self.driver).move_to_element(above).perform()
