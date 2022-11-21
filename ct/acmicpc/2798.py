N, M = map(int, input().split())
card = list(map(int, input().split()))

temp = 0

for i in range(N):
    for j in range(i, i+3):
        temp += card[i]