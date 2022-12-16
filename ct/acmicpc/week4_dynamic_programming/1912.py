N = int(input())
array = list(map(int, input().split()))

for i in range(1, N):
    array[i] = max(array[i], array[i] + array[i - 1])

print(max(array))
