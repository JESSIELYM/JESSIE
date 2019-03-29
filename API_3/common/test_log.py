import logging   #logging模块时Python自带的，直接导入使用
from 接口自动化.API_3.common import project_path
from 接口自动化.API_3.common import TestConfig
class MyLog:   #定义一个日志类
    def __init__(self):
        self.logger_name=TestConfig.ReadConfig(project_path.config_ini_path).get_str('log_set', 'logger_name')
    def mylog(self,level,message):
        my_logger=logging.getLogger(self.logger_name)  #定义一个收集器,从配置文件中获取收集器名字
        my_logger.setLevel('INFO')  #设置级别
        formatter=logging.Formatter('[%(asctime)s]-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')  #定义一个日志输出格式,可以自己加中括号或者加些其他符号
        ch=logging.StreamHandler()   #设置控制台输出渠道
        ch.setLevel('ERROR')    #设置级别   当日志收集级别和输出渠道级别不一致时，取交集
        ch.setFormatter(formatter)  #按formatter格式输出日志到控制台
        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')  #设置文件输出渠道，文件追加方式默认为a，即日志会追加到文件末尾，如果模式不是a，则会覆盖清空之前的日志，与open函数的追加是一个意思
        fh.setLevel('INFO')
        fh.setFormatter(formatter)   #按formatter格式输出日志到文件
        my_logger.addHandler(ch) #my_logger这日志收集器要增加ch这个输出渠道
        my_logger.addHandler(fh)
        if level=='DEBUG':
            my_logger.debug(message)
        elif level=='INFO':
            my_logger.info(message)
        elif level =='WARNING':
            my_logger.warning(message)
        elif level == 'ERROR':
            my_logger.error(message)
        elif level == 'CRITICAL':
            my_logger.critical(message)
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)
    def debug(self,message):
        self.mylog('DEBUG',message)
    def info(self,message):
        self.mylog('INFO',message)
    def warning(self, message):
        self.mylog('WARNING', message)
    def error(self, message):
        self.mylog('ERROR', message)
    def critical(self, message):
        self.mylog('CRITICAL', message)
if __name__=='__main__':
    # MyLog().mylog('ERROR','停电了')  #类的实例化，调用函数
    test_logger=MyLog()
    test_logger.debug('我是一个优化后的DEBUG信息')
    test_logger.error('我是一个优化后的ERROR信息')
