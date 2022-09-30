

import unittest
from unittestreport import TestRunner

# 加载测试套件
case_dir = '../testcase/'
discover = unittest.defaultTestLoader.discover(case_dir, 'test*.py')
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testcase)
# 执行测试用例
runner = TestRunner(suite=discover, title='自动化测试报告', tester='99', desc="UI自动化测试报告", templates=2)
# runner.run(tread_count=3)这是多线程去跑
# 执行所有用例，并且失败重试，不用每个用例去加rerun标签
#runner.rerun_run(count=0, interval=3) #重试次数
runner.run()
# 发邮件功能:password是授权码，
runner.send_email(host="smtp.qq.com", port=25, user="576648349@qq.com", password="rhroscgdwzcgbdbb",
                  to_addrs=["chenshanshan99666@163.com"])