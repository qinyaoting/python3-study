#!/usr/bin/python3

# 偏函数

print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

# 如果要转换大量的二进制字符串, 每次都传入int(x, base=2)非常麻烦

def int2(x, base=2):
    return int(x, base)

print(int2('1000101010'))


# 偏函数就是帮我们简化定义int2()方法

import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
