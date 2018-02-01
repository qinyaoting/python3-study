#!/usr/bin/python3

# 列表生成式

# 用range生成列表
li = list(range(1,11))
print(li)

# 用for生成列表
L = []
for i in li:
    L.append(i)
print(L)

# 用列表生成式
li = [x for x in range(0, 101)]
print(li)

#  打印 1X1, 2X2, 3X3....
print([x*x for x in range(1, 11)])


# 生成0-100的偶数
li = [x for x in range(0,101) if x%2==0]
print(li)


# 用两层循环生成全排列
lis = [x+y for x in 'ABC' for y in 'XYZ']
print(lis)

# 列出目录和文件
import os
print([d for d in os.listdir('..')])

# 使用两个变量来生成list
d = {'Jack':'boy', 'Lucy':'girl', 'puppy':'pet'}
print([k + '-' + v for k, v in d.items()])

# 把list的所有字符改为小写
L = ['Hello', 'Jack', 'Tom', 'has', 'lost']
print([s.lower() for s in L])
