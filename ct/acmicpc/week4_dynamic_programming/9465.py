import sys
input = sys.stdin.readline

for case in range(int(input())):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]
    dp = array[:]

    if n == 1:
        print(max(dp[0]) if max(dp[0]) > max(dp[1]) else max(dp[1]))
        break

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0]) if max(dp[0]) > max(dp[1]) else max(dp[1]))


# [0][i] 에서 스티커를 제거할 시, [1][i-1] or [1][i-2] 의 최대값과 매치된다.