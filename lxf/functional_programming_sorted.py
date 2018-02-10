#!/usr/bin/python3

# sorted


print(sorted([36, 5, -12, 9, -21]))

# 根据绝对值排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 因为'a'<'Z', 对字符串排序是按照ascii的值比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反序o
print((sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda x:(x[0].lower(), x[1])))


