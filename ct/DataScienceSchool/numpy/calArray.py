import numpy as np

x = np.arange(1, 10001)
y = np.arange(10001, 20001)
'''
z = np.zeros_like(x)
for i in range(10000):
    z[i] = x[i] + y[i]
''' 
z = x + y
print(z[:10])

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])

print(np.all(a == b))
print(np.all(a == c))

x = np.arange(5)
print(x)
y = np.ones_like(x)
print(y)
print(x+y)
print(x+1)

x = np.vstack([range(7)[i:i + 3] for i in range(5)])
print(x)
y = np.arange(5)[:, np.newaxis]
print(y)
print(x+y)