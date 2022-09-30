from selenium.webdriver.common.by import By

from base.base_page import BasePage
import page_object.login_page
from selenium import webdriver
import json
import common.global_var
import time


class AddMeetingRoom(BasePage):
    def getcookie(self):
        with open('../Data/mycookie.txt','r') as f:
            tmp = json.loads(f.read())
            return tmp
    def add(self):
        self.driver = common.global_var.get_value('gdriver')
   #     self.driver.add_cookie(self.getcookie())
      #  self.open('https://vip.xylink.com/console/management#/business')
        #页面元素
        self.meetingcontrol = {By.XPATH,'/html/body/div[1]/section/main/div/aside/div/ul/li[3]/div/span'}
        self.meetingroom = {By.XPATH,'/html/body/div[1]/section/main/div/aside/div/ul/li[3]/ul/li[5]/span'}
        self.add = {By.XPATH, '//*[@id="drag-content"]/section/main/div/div/div/div/div[2]/div/div/span[1]/button'}
        self.meetingname = {By.XPATH,'//*[@id="name"]'}

        self.assertok = {By.XPATH,'/html/body/div[11]/div/div[2]/div/div/div[2]/div[2]/span[2]/button'}
        time.sleep(3)
        self.click(self.meetingcontrol)
        time.sleep(3)
        self.click(self.meetingroom)
        time.sleep(3)
        self.click(self.add)
        self.input_(self.meetingname,"test")
        self.click(self.assertok)

