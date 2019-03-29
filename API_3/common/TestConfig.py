#写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串
from configparser import ConfigParser
from 接口自动化.API_3.common import  project_path
class ReadConfig:
    def __init__(self,file_name):
        self.cf=ConfigParser()
        self.cf.read(file_name,encoding='utf-8')
    def get_int(self,section,option):
        '''从配置文件里获取一个整数'''
        value=self.cf.getint(section,option)
        return value
    def get_float(self,section,option):
        '''从配置文件里获取一个浮点数'''
        value = self.cf.getfloat(section,option)
        return value
    def get_boolean(self,section,option):
        '''从配置文件里获取一个布尔值'''
        value = self.cf.getboolean(section,option)
        return value
    def get_str(self,section,option):
        '''从配置文件里获取一个字符串'''
        value = self.cf.get(section,option)
        return value
    def get_data(self,section,option):
        '''从配置文件里获取一个元祖 字典 列表的数据'''
        value = self.cf.get(section,option)
        return eval(value)

if __name__=='__main__':
    res=ReadConfig(project_path.config_ini_path).get_str('log_set','level')
    print(res)