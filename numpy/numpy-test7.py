import numpy as np

'''
copy deep copy
'''
a = np.arange(4)
print(a)

b = a
c = a
d = b

a[0] = 11
print(a)
print(b)

print(a is b)

d[1:3] = [22, 33]
print(a)
print(d)

b = a.copy()  # deep copy
print(a)
print(b)
a[3] = 44
print(a)
print(b)
