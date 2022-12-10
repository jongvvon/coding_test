import sys
input = sys.stdin.readline

num = int(input())
fibonacci = [0] * (num + 2)
fibonacci[0] = 0
fibonacci[1] = 1

for i in range(2, num + 2):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

print(fibonacci[num])
