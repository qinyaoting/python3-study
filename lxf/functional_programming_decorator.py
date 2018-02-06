#!/usr/bin/python3

# 装饰器



# 不修改now方法的同时, 给它添加自动打印日志的功能
# 在代码运行期间动态增加功能的方式, 称之为装饰器Decorator

# 定义了一个log方法, 方法里边又定义了wapper方法, 并将其返回
def log(func):
    def wapper(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wapper   # 返回没有括号

@log # 增加@log相当于now = log(now)
def now():
    print('2017-01-01')


f = now
print("=========")
f()

# 输出函数的名字
# print(now.__name__)
# print(f.__name__)

# 感慨: 一套多层就晕啊
def log_with_args(text):
    def decorator(func):
        def wapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wapper
    return decorator

@log_with_args('execute') #now = log('execute')(now)
def now2():
    print('111111')

now2()

#???
import functools
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
