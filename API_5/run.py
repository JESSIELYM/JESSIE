import  unittest
from 接口自动化.API_5.test_results.test_report import HTMLTestRunnerNew
from 接口自动化.API_5.test_case import test_register  #导入用例模块
from 接口自动化.API_5.test_case import test_recharge
from 接口自动化.API_5.test_case import test_withdraw
from 接口自动化.API_5.common import project_path

# 新建一个测试集
suite=unittest.TestSuite()
# 添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))  #从模块导入用例
suite.addTest(loader.loadTestsFromModule(test_recharge))  #从模块导入用例
suite.addTest(loader.loadTestsFromModule(test_withdraw))  #从模块导入用例
# 执行用例 生成测试报告
with open(project_path.report_path,'wb') as file:    #写内容到html文件里面去的话，要用wb的方式，且wb模式不需要encoding编码，因为wb是二进制的写法
    # stream 报告要写到哪里去，verbosity报告详细程度  title 报告标题   description报告描述  tester 测试者
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='2019年3月27日接口自动化测试报告',
                                              description='完成前程贷的登录及注册的第5阶段的接口测试',
                                              tester='JESSIE')
    runner.run(suite) #执行用例，传入suite里收集的测试用例