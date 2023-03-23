n = int(input())
headcount = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
temp = 0
for i in range(n):
    headcount[i] = headcount[i] - b
    cnt += 1
    if headcount[i] > 0:
        temp = headcount[i] % c
        cnt += headcount[i] // c
        if temp != 0:
            cnt += 1

print(cnt)