import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])

# 上下合并
c = np.vstack((a,b))
print(c)

print(a.shape)
print(c.shape)

# 左右合并
d = np.hstack((a,b))
print(d)

print(a.T)
print(a[np.newaxis, :])
print(a[:, np.newaxis])

e = np.concatenate((a,b,b,a))
f = np.concatenate((a,b,b,a), axis=0)
print(e)
print(f)
