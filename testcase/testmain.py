import unittest

from page_object.add_meetingroom_page import AddMeetingRoom
from page_object.login_page import LoginPage
import common.global_var
from page_object.newcoder import testnowcoder


class Testcase(unittest.TestCase, LoginPage,AddMeetingRoom,testnowcoder):

    def setUp(self) -> None:
        print("开始前")
        self.username = '17712345615'
        self.passwd = '000000'

    def test_01(self):
        common.global_var._init()
        self.login(self.username, self.passwd)
       # self.add()

        #self.login_newcoder()
        #self.openother()
        #self.openbaidu()

    # 恢复环境
    def tearDown(self) -> None:
        print("结束")
       # self.close()
        self.close()