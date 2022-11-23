N, X = map(int, input().split())
nums = list(map(int, input().split()))

for i in nums:
    if i < X:
        print(i, end=" ")
