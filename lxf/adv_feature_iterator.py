#!/usr/bin/python3

# 迭代器iterator和迭代是不同的iteration

from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 生成器可以作用于for, 可以next()函数, 知道最后一个元素抛出StopIteration错误

print("===========================================j")
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# Iterator的计算是惰性的
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


