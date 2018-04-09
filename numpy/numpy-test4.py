import numpy as np

a = np.arange(3, 15)
# print(a)

# print(a[3])


b = np.arange(3, 15).reshape((3, 4))
print(b)

# 输出第3行
# print(b[2])

# 输出第二行第二列的元素, 可以放到一个[]中, 用逗号分割
# print(b[1][1])
# print(b[1, 1])

# 输出第三列
# print(b[2, :])

# 输出第一列
# print(b[:, 0])

# 输出第2行, 第二列
# print(b[1, 1:2])

for row in b:
    print('---', row)


for column in b.T:
    print('===', column)

# b矩阵拍扁
print(b.flatten())
for item in b.flat:
    print(item)
