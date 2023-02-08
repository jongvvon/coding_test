import sys
input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]

dp = [[0 for _ in range(3)] for _ in range(n + 1)]

#[i][0] -> 와인을 안마시는 경우 / [i][1] -> 와인을 첫번째 마시는 경우 / [i][2] -> 와인을 두번째 마시는 경우
for i in range(n + 1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + wines[i]
    dp[i][2] = dp[i-1][1] + wines[i]

# print(wines)
# print(dp)
print(max(dp[-1]))