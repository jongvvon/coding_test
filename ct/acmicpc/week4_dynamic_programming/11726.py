dp = [0] * 1001


def tiling(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dp[n] != 0:
        return dp[n]
    dp[n] = tiling(n-2) + tiling(n-1)
    return dp[n]


num = int(input())
print(tiling(num) % 10007)