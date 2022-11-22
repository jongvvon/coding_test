N, M = map(int, input().split())
card = list(map(int, input().split()))
nearNum = 0
temp = {}
for i in range(0, len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            nearNum = card[i]+card[j]+card[k]
            if nearNum <= M:
                temp[nearNum] = M - nearNum

print(temp)
print(min(temp, key=temp.get))