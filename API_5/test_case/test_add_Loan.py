import  unittest
from ddt import ddt,data
from 接口自动化.API_5.common.http_request import HttpRequests
from 接口自动化.API_5.common.do_excel import DoExcel
from 接口自动化.API_5.common import project_path
from 接口自动化.API_5.common.test_log import MyLog
from 接口自动化.API_5.common.get_data import GetData

# 测试充值
test_data = DoExcel(project_path.case_path, 'add_Loan').Read_Excel('Add_Loan_CASE')
# COOKIES=None  #设定COOKIES作为一个全局变量
@ddt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.t = DoExcel(project_path.case_path, 'add_Loan')
    def tearDown(self):
        pass
    @data(*test_data)
    def test_cases(self,case):
        global TestResult     #声明全局变量
        # global COOKIES
        # 执行用例
        http = case['Url']
        Method = case['Method']
        param =eval(case['Params'])
        # print(type(param))
        # 发起测试
        print('-----------------正在测试{}模块里的第{}条测试用例---------------------'.format(case['Module'],case['CaseID']))
        # MyLog().info('正在执行{}模块的第{}条测试用例'.format(Module, CaseID))
        resp = HttpRequests().requests(http, Method,param,cookies=getattr(GetData,'COOKIE'))
        print('实际结果：{}'.format(resp.json()))   #发送请求拿到的实际返回值
        # MyLog().info('实际结果是：{}'.format(resp.json()))  # http发送请求拿到的实际返回值
        # 加一个判断：
        if resp.cookies:   #判断请求的cookie是否为空
           setattr(GetData,'COOKIE',resp.cookies)   #使用反射来更新COOKIES的值
        # 对比结果
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult = 'Pass'
        except AssertionError as e:
            MyLog().error('在执行{}模块的第{}条测试用例时，实际结果与预期结果对比出错了，错误内容是{}'.format(case['Module'], case['CaseID'], e))
            TestResult = 'Failed'
            raise e
        finally:
            MyLog().info('开始向EXCEL中写入第{}条用例的测试结果'.format(case['CaseID']))
            self.t.Write_back(case['CaseID'] + 1, 8, resp.text)
            self.t.Write_back(case['CaseID'] + 1, 9, TestResult)
