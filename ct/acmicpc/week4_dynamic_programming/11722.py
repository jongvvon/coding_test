num = int(input())
array = list(map(int, input().split()))

dp = [0] * num
for i in range(num):
    for j in range(i):
        if array[i] < array[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
