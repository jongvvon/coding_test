import math

A, B = map(int, input().split())
n = 1000000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for k in range(A, B+1):
    if array[k]:
        print(k)
