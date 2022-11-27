import math

n = 123456 * 2
array = [True for i in range(n+1)]
array[0], array[1] = False, False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

flag = True
while flag:
    num = int(input())
    cnt = 0
    if num == 0:
        flag = False
        break
    if num == 1:
        cnt += 1
    for k in range(num+1, 2*num):
        if array[k]:
            cnt += 1
    print(cnt)
