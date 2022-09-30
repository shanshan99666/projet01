# coding=utf-8


import time
from time import sleep
from log.getLogStream import logStream

from selenium.webdriver.common.action_chains import ActionChains

log = logStream()


# 创建基类
class BasePage:
    # driver = webdriver.Chrome()
    # 构造函数
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver

    # 访问URL
    def open(self, url):
        log.info('访问网址')
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(1)

    # 元素定位
    def locator(self, loc):
        log.info('正在定位{}元素'.format(loc))
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):

        try:
            log.info('正在定位{}元素， 输入{}内容'.format(loc, txt))
            self.locator(loc).send_keys(txt)
            sleep(2)
        except Exception as e:
            self.screenShot()
            log.error('错误日志' % e)

    # 点击
    def click(self, loc):

        try:
            log.info('正在点击{}元素'.format(loc))
            self.locator(loc).click()
        except Exception as e:
            self.screenShot()
            log.error('错误日志' % e)

    # 等待
    def wait(self, time_):

        log.info('等待时间{}秒'.format(time_))
        sleep(time_)

    # 关闭
    def quit(self):

        log.info('退出')
        self.driver.quit()

    # 最大化
    def maxSize(self):

        log.info('最大化')
        self.driver.maximize_window()

    # 截图并保存
    def screenShot(self):

        current_time = time.strftime('%Y-%m-%d %H-%M-%S')
        print(current_time)
        pic_path = '../log/screenshot' + '/' + current_time + '.png'
        self.driver.save_screenshot(pic_path)

    # 关闭浏览器
    def close(self):

        self.driver.close()

    # 刷新浏览器
    def refresh(self):

        self.driver.refresh()

    def waitUntilPageContains(self, message):

        log.info('正在获取页面%s字段' % message)
        sleep(3)
        msg = self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % message).text
        print(msg)
        return msg


    def mouseperform(self,loc):

        # ele = self.locator(loc)
        # time.sleep(3)
        # ActionChains(self.driver).move_to_element(ele).perform()

        ele = self.locator(loc)
        #time.sleep(2)
        ActionChains(self.driver).move_to_element(ele).perform()

        log.info("悬停鼠标到", loc)

