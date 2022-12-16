N = int(input())
array = list(map(int, input().split()))

dp = array[:]
for i in range(N):
    for j in range(i):
        if array[i] > array[j] and dp[i] < dp[j] + array[i]:
            dp[i] = dp[j] + array[i]
print(max(dp))
