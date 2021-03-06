import requests
from 接口自动化.API_3.common.test_log import MyLog
class HttpRequests:
    '''该类完成http的get以及post请求，并返回结果'''
    def requests(self,http,Method,param,cookies):
        '''该函数根据传入参数来发起请求
           http:接口地址
           Method：请求方式
           param：请求参数
        '''
        global COOKIES
        if Method.upper()=='GET':
            MyLog().info('正在发起GET请求')
            try:
                resp=requests.get(url=http,params=param,cookies=cookies)  #发起get请求，获取cookies,返回一个消息实体
            except Exception as e:
                MyLog().error('发起GET请求出错了,错误信息是：{}'.format(e))
        elif Method.upper()=='POST':
            MyLog().info('正在发起POST请求')
            try:
                resp = requests.post(url=http,data=param,cookies=cookies)  # 发起post请求
            except Exception as e:
                MyLog().error('发起POST请求出错了,错误信息是：{}'.format(e))
        else:
            print('请求方式出错')
            resp=None
        # MyLog().info('请求得到的内容是{}'.format(resp.text))
        return resp  #输出请求体

if __name__=='__main__':
    http= 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    Method='get'
    param={'mobilephone':'15600000000','pwd':'12345'}
    res=HttpRequests().requests(http, Method, param)
    # print(res.requests(http,Method,param).json())
    print(res)
    print(res.cookies)

