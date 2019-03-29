import os
# 文件的路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)
# 测试用例的路径
case_path=os.path.join(project_path,'test_case','接口自动化测试用例.xlsx')
# print(case_path)
# 配置文件的路径
config_ini_path=os.path.join(project_path,'conf','ReadConfig.ini')
# print(config_ini_path)
# 读取配置文件的类路径
TestConfig_path=os.path.join(project_path,'common','TestConfig')
# print(TestConfig_path)
# 编写日志类的路径
test_log_path=os.path.join(project_path,'common','test_log')
# print(test_log_path)
# 日志文件存储路径
log_path=os.path.join(project_path,r'test_results\test_log','test.log')
# print(log_path)
# 测试报告的存储路径
report_path=os.path.join(project_path,r'test_results\test_report','TestReport.html')