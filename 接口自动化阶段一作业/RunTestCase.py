import unittest
from 单元测试 import HTMLTestRunnerNew
from 接口自动化.接口自动化阶段一作业 import AddTestCase
loader=unittest.TestLoader()
suite=unittest.TestSuite()
suite.addTest(loader.loadTestsFromModule(AddTestCase))
with open('TestReport_20190311.html','wb') as file:    #写内容到html文件里面去的话，要用wb的方式，且wb模式不需要encoding编码，因为wb是二进制的写法
    # stream 报告要写到哪里去，verbosity报告详细程度  title 报告标题   description报告描述  tester 测试者
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='2019年3月8日接口自动化测试报告',
                                              description='完成前程贷的登录及注册的接口测试',
                                              tester='JESSIE')

    runner.run(suite)