# 定义闭包函数：双层函数，内置函数必须引用外函数的参数
def outer():
    a = 100

    def inner():
        b = 200
        print('a= ', a)
        print('b= ', b)

    return inner


func = outer()  # func = inner
func()  # inner()


# 装饰器：在不更改被装饰函数的内容的前提下，增加其他功能目的
# 1. 外函数中必须定义一个函数
# 2. 内函数必须使用外函数的局部变量
# 3. 外函数必须返回内函数的引用

# 装饰器引用
# @outer @后边跟装饰器函数名

# 装饰器原理
# 装饰过程原理： show = outer(show)

# 装饰器内函数参数 *args，**kwargs
# 被装饰的函数结果是return时，装饰器内函数把执行函数赋值并返回
def outere(funn):
    def inner(*args, **kwargs):
        print('执行前的装饰代码')
        resoult = funn(*args, **kwargs)
        print('执行后的装饰代码')
        return resoult

    return inner


@outere
def show():
    ss = 'show now....'
    return ss


a = show()
print(a)
print(show)


# 面向对象
class Myclass:  # 关键字：class，类名 Myclass，首字母大写
    # __new__：申请内存空间方法，会调用 __init__方法
    def __init__(self, name):  # 初始化方法,自动调用
        self.name = name

    # 所有实例方法都有 self
    #
    def upper(self):
        print('upper' + self.name)  # 调用初始化参数
        # 函数默认自带输出 return None

    def lower(self):
        print('lower' + self.name)

    def __repr__(self):
        return f'my name is {self.name} +1+1+1+1'

    def __str__(self):
        return self.__repr__()
    # def __str__(self): # 执行返回内容格式
    #     # 必须要返回一个字符串
    #     # 系统自带的魔法属性与魔法方法
    #     return f'my name is {self.name}'


obj = Myclass('asd')
obj2 = Myclass('dfrg')
# print(obj.upper())
# print(obj.lower())
# print(f'obj.name= {obj.name}')
# print(f'obj2.name= {obj2.name}')
Myclass.upper(obj2)
print(Myclass.__dict__)
