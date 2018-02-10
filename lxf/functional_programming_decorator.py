#!/usr/bin/python3

# 装饰器

# 不修改now方法的同时, 给它添加自动打印日志的功能
# 在代码运行期间动态增加功能的方式, 称之为装饰器Decorator

# 定义了一个log方法, 方法里边又定义了wrapper方法, 并将其返回
import signal
from time import sleep


def log(func):
    def wraps(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wraps   # 返回没有括号


@log # 增加@log相当于now = log(now)
def now():
    print('2017-01-01')


# 带参数的装饰器, 需要多定义一层, 感慨: 一套多层就晕啊
def log_with_args(text):
    def decorator(func):
        def wraps(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wraps
    return decorator


# 如何使用带有参数的装饰器
@log_with_args('execute') #now = log('execute')(now)
def now2():
    print('111111')


# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
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


def time_limit(interval):
    def wraps(func):
        def handler():
            raise RuntimeError()
        def deco(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(interval)
            res = func(*args, **kwargs)
            signal.alarm(0)
            return res
        return deco
    return wraps


@time_limit(5)
def test_timeout():
    sleep(9)


if __name__ == '__main__':
    f = now
    f()
    # 输出函数的名字
    # print(now.__name__)
    # print(f.__name__)
    print("=========")
    now2()
    print("=========")

    # 模拟运行超时报错
    try:
        test_timeout()
    except RuntimeError as e:
        print('ex')