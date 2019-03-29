from 接口自动化.API_1.common.do_excel import DoExcel
from 接口自动化.API_1.common.http_request import HttpRequests
from 接口自动化.API_1.common import project_path
from 接口自动化.API_1.common.test_log import MyLog
# 读取测试用例
file=project_path.case_path
sheet='API_01_TC'
test_data=DoExcel(file,sheet).Read_Excel()
# print(test_data)
# 执行用例
for case in test_data:
    CaseID=case['CaseID']
    Module=case['Module']
    http=case['Url']
    Method=case['Method']
    param=eval(case['Params'])
    # 发起测试
    MyLog().info('正在执行{}模块的第{}条测试用例'.format(Module,CaseID))
    resp=HttpRequests().requests(http,Method,param)
    MyLog().info('实际结果是：{}'.format(resp.json()))  #http发送请求拿到的实际返回值
# 对比结果
    try:
        if resp.json()==eval(case['ExpectedResult']):
            TestResult='Pass'
        else:
            TestResult='Failed'
        MyLog().info('该条测试用例测试结论：{}'.format(TestResult))
    except Exception as e:
        MyLog().error('在执行{}模块的第{}条测试用例时，实际结果与预期结果对比出错了，错误内容是{}'.format(Module,CaseID,e))

# 写回结果
    MyLog().info('开始向EXCEL中写入第{}条用例的测试结果'.format(CaseID))
    t=DoExcel(file,sheet)
    t.Write_back(case['CaseID']+1,8,resp.text)
    t.Write_back(case['CaseID']+1,9,TestResult)

