num = int(input())
score = list(map(int, input().split()))
temp = 0

for i in range(num):
    temp += (score[i] / max(score) * 100)

print(temp / num)