dp = [0] * 91
dp[1], dp[2] = 1, 1


def pinary_num(n):
    if n < 3:
        return dp[n]
    else:
        if dp[n] != 0:
            return dp[n]
        dp[n] = pinary_num(n - 2) + pinary_num(n - 1)
        return dp[n]


num = int(input())
print(pinary_num(num))