total = int(input())
num = int(input())
temp = 0
for _ in range(num):
    prize, count = map(int, input().split())
    temp += prize * count

print("Yes" if temp == total else "No")
