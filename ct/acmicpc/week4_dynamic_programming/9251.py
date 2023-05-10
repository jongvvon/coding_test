"""
금일 코테 인증 23.05.10

관련 문제 <백준 9251: LCS> (완료)

문제 요약
Longest Common Subsequence 문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제

해결 방법 및 추가 정보
해당 점화식을 찾는데 시간이 조금 걸렸고 "부분 수열" 이라는 정확한 의미 해석에 시간을 좀 쓴 문제같다.
대략적인 풀이의 경우 사진으로 첨부했다.
"""

import sys

string_a = ' ' + sys.stdin.readline().rstrip()
string_b = ' ' + sys.stdin.readline().rstrip()
dp = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_a[i] == string_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])