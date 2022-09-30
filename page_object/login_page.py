from time import sleep

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium import webdriver
import json
import common.global_var
import time

class LoginPage(BasePage):

    def login(self, username, password):

        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(10)

        common.global_var.set_value("gdriver",self.driver)

        self.url = "https://vip.xylink.com/console/management#/login"

        # 页面元素
        self.user = (By.ID, "account_username")
        self.passwd = (By.ID, 'account_password')
        self.button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/form/span/button')
        # 访问URL,最大化
        self.open(self.url)

        self.input_(self.user, username)
        # 输入密码
        self.input_(self.passwd, password)
        # 点击登录按钮
        self.click(self.button)
        time.sleep(5)
        self.getcookie()


    def getcookie(self):
        with open("../Data/mycookie.txt","w+") as f:
            f.write(json.dumps(self.driver.get_cookies()))