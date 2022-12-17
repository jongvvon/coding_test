n = int(input())
array = [0 for _ in range(n)]
for i in range(n):
    array[i] = list(map(int, input().split()))

dp = array[:]
dp[1][0] += dp[0][0]
dp[1][1] += dp[0][0]
for i in range(2, n):
    for j in range(i+1):
        if j == 0:
            dp[i][0] = dp[i-1][0] + array[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][i-1] + array[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

print(max(dp[-1]))