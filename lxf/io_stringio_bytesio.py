#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'chin'

# StringIO BytesIO



if __name__ == '__main__':

    # StringIO 可以在内存中读写字符串
    from io import StringIO
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())
    f.close()

    ff = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = ff.readline()
        if s == '':
            break
        print(s.strip())
    # BytesIO如果操作二进制数据, 就要使用BytesIO
    from io import BytesIO
    fff = BytesIO()
    fff.write('中午'.encode('utf-8'))
    print(fff.getvalue())

    f4 = BytesIO(b'\xe4\xb8\xad\xe5\x8d\x88')
    print(f4.read())