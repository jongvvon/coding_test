# recursive
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# top-down (memoization)
def fibonacci(n, memo):
    if n <= 1:
        return n
    if memo[n] == 0:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 10
memo = [0]*(n+1)

# bottom-up (tabluation)
def fibonacci(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 10


def solution(n):
    answer = fibonacci(n)
    return answer