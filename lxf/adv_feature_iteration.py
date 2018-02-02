#!/usr/bin/python3

# 迭代

L = [1,2,3,4]
for i in L:
    print(i)

# 不光list tuple 可以迭代, str dict也可以
for s in 'ABC':
    print(s)

# 遍历dict的k或者v
d = {'Jack':'boy','Lucy':'girl','puppy':'pet'}
for key in d:
    print ("key=" , key)

for v in d.values():
    print(v)

# 同时便利dict的k,v
for k,v in d.items():
    print("%s-%s" % (k,v))

# 因为list, 如果想要根据索, 可以把他转换为枚举

for i,v in enumerate(['A','B','C']):
    print('%d=%s' % (i,v))

# 判断一个对象是否是Iterable类型
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

# 同时引用两个变量
for x,y in [(1,1), (2,4), (3,9)]:
    print(x,y)
