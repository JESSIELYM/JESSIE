import requests
# from 接口自动化.接口自动化阶段一作业.Run import ImportTestCase
class HttpRequests:
    '''该类完成http的get以及post请求，并返回结果'''
    def requests(self,http,Method,param):
        '''该函数根据传入参数来发起请求
           http:接口地址
           Method：请求方式
           param：请求参数
        '''
        if Method.upper()=='GET':
            resp=requests.get(url=http,params=param)  #发起get请求，返回一个消息实体
        elif Method.upper()=='POST':
            resp = requests.post(url=http,data=param)  # 发起post请求
        else:
            print('请求方式出错')
            resp=None
        return resp  #输出请求体

if __name__=='__main__':
    http= 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    Method='get'
    param={'mobilephone':'15671638341','pwd':'12345'}
    res=HttpRequests().requests(http, Method, param)
    # print(res.requests(http,Method,param).json())
    print(res.text)
    print(res.cookies)

