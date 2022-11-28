import math

n = 10000
array = [True for i in range(n+1)]
array[0], array[1] = False, False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

T = int(input())

for case in range(0, T):
    num = int(input())
    flag = True
    for i in range(num//2, num):
        if not array[i]:
            continue
        for j in range(num//2, 1, -1):
            if not array[j]:
                continue
            if i + j == num:
                print(j, i)
                flag = False
                break
        if not flag:
            break


