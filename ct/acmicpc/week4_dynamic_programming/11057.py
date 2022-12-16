num = int(input())
mod = 10007
dp = [[0 for _ in range(10)] for _ in range(num)]
dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, num):
    for j in range(9, -1, -1):
        if j == 9:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j+1] + dp[i-1][j]

print(sum(dp[num - 1]) % mod)