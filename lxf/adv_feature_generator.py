#!/usr/bin/python3

# 生成器是什么?
# 用list存放一个很大的序列, 非常占内存, 如果边循环, 边计算得到要的值, 非常节省内存
# 把[] 改为 ()就变成生成器了

# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，
# 并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，
# 就是结束generator的指令，for循环随之结束。

# 普通方法 如果含有yield就变成生成器了, 调用generator方法,需要把方法传入到next()中,
# 调用generator方法, 碰到yield就返回, 再调用一次,从上次返回的地方继续往下


def gen():
    print("1")
    yield 1
    print("2")
    yield(2)
    print("3")
    yield(3)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"


if __name__ == '__main__':

    d = [x*x for x in range(10)]
    print(d)

    gx = (x*x for x in range(10))
    print(gx) #<generator object <genexpr> at 0x7f5ef04d3f68>

    ge = gen()
    #next(ge)

    # next(ge) StopIteration 到最后一个元素会抛出错误
    # 一般也不这么调用,采用for

    for x in (x*x for x in range(10)):
        print('x = %s' % x)

    # 遍历斐波那契数列
    for n in fib(6):
        print(n)

    # 拿不到return 这么办
    g = fib(6)
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print(e.value)
            break
