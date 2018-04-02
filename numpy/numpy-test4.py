import numpy as np
a = np.arange(3, 15)
print(a)

print(a[3])


b = np.arange(3,15).reshape((3,4))
print(b)

# 输出第3行
print(b[2])

print(b[1][1])
print(b[1,1])
print(b[2,:])
print(b[:,0])
print(b[1,1:2])

for row in b:
    print(row)


for column in b.T:
    print(column)


print(b.flatten())
for item in b.flat:
    print(item)
