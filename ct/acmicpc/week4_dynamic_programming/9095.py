dp = [0] * 11


def ott_sum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if dp[n] != 0:
        return dp[n]
    dp[n] = ott_sum(n-3) + ott_sum(n-2) + ott_sum(n-1)
    return dp[n]


for case in range(int(input())):
    num = int(input())
    print(ott_sum(num))