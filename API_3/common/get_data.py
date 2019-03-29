class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIE=None

# 类属性
# print(GetData.COOKIE)
# print(GetData().COOKIE)

# 利用反射的方法来拿值
# print(getattr(GetData,'COOKIE'))   #getattr 获取属性值，第一个参数是类名，第二个参数是属性的参数名
# print(hasattr(GetData,'COOKIE'))  #判断属性值是否存在，第一个参数是类名，第二个参数是属性的参数名，返回的是布尔值
# setattr(GetData,'COOKIE','123456')  #判断属性值是否存在，第一个参数是类名，第二个参数是属性的参数名，第三个参数是要设置的新值
# print(getattr(GetData,'COOKIE')) #设置完后再来获取值会发现值已经变化
# delattr(GetData,'COOKIE')   #删除类的某个属性，不常用
# print(getattr(GetData,'COOKIE')) #删除后再来获取值会报错显示没有属性值