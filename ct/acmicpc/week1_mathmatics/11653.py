import math

n = 100000
array = [True for i in range(n+1)]
array[0], array[1] = False, False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

