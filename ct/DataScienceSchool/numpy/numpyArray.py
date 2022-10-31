import numpy as np
'''
ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = []
for di in data:
    answer.append(2 * di)
print(answer)

x = np.array(data)
print(x)
print(2 * x)

c = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array
print(c)
'''

# pratice 1
a = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(a)

# pratice 2
m = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])
# 2-1. indexing 7
print(m[1][2])
# 2-2. indexing 14
print(m[2][4])
# 2-3. slicing [6, 7]
print(m[1, 1:3])
# 2-4. slicing [7, 12]
print(m[1:3, 2])
# 2-5. slicing [[3,4], [8,9]]
print(m[0:2, 3:5])

# pratice 3
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# 3-1. Find multiple of 3
print(x[x % 3 == 0])
# 3-2. Find the number that leaves 1 when divided by 4.
print(x[x % 4 == 1])
# 3-3. Find a number that divides by 3 and leaves a remainder when divided by 4.
print(x[(x % 3 == 0) & (x % 4 == 1)])


# datatypes of Numpy
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.T)

a = np.arange(12)
print(a)
b = a.reshape(3, 4)
print(b)
# 다차원 배열을 무조건 1차원으로 만들기 위해서는 
# flatten 나 ravel 메서드를 사용한다.

x = np.arange(3)
print(x)

y = np.arange(5)
print(y)

X, Y = np.meshgrid(x, y)
print(X)
print(Y)


