import math

n = 1000000
array = [True] * (n + 1)
array[0], array[1] = False, False
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i * j <= n:
        array[i * j] = False
        j += 1

for case in range(0, int(input())):
    num = int(input())
    cnt = 0
    for j in range(1, num//2+1):
        if array[j] and array[num-j]:
           cnt += 1
    print(cnt)