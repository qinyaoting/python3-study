#!/usr/bin/python3

#编码
#默认是UTF-8,可以指定编码
#                       # -*- coding: cp-1252 -*-

#标识符
#第一个字符必须是字母或者下划线
#标识符其他可以是字母数字下划线
#大小写敏感
#python3非ascii也是允许的

#保留字
import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 单行注释以#开头, 第一个注释
print("Hello, World")


# 注释1
# 注释2
'''
多行注释用三个单引号
'''
"""
多行注释也可以用三个双引号
"""

# 行与缩进
# 用缩进来代表代码块,不使用括号

if True:
    print("True")
else:
    print("False")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  # print("False")#缩进不一致会导致错误

# 多行语句
'''
total = item_one + \
        item_two + \
        item_three
'''

# 在[] {} ()中的多行语句, 不需要使用反斜杠
total = ['item_one', 'item_two', 'item_three'
        'item_four', 'item_five']

# 数据类型
# 数有四种类型:整数 长整数 浮点数和复数
'''
1 
1.23 
3E-2 
1+2j 
1.1+2.2j
'''

# 字符串
# 单引号与双引号使用----完全相同
# 三引号指定多行字符串
# 转译符
# 自然字符串,r R r"this is a line with \n" \n会显示,不是换行
# 允许处理unicode字符串 u U u"this is an unicode string"
# 字符串是不可变的
# 按字面意义级联字符串"this" "is" "string" 会自动转换为this is string
word = '字符串'
sentence = '这是一个句子'
paragraph = '''这是一个段落
可以有多行组成'''

'''
空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
'''
# 等待用户输入
# input("\n\n按下enter后退出:")

# 同一行显示多条语句, 要一分号分割
import sys; x = 'runoob'; sys.stdout.write(x+'\n')

x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
# 不换行输出
print(x, end=' ')
print(y, end='')
print()

# import 与 from...import
'''
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *]
'''

import sys
print("===============")
print("命令行参数为:")
for i in sys.argv:
    print(i)
print('\n python路径为',sys.path)

from sys import argv,path  #  导入特定的成员
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

