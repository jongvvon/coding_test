"""
가중치가 없는 경우 DP를 이용한 최단 경로의 개수를 구할 수 있다.
이동은 오직 오른쪽이나 아래로만 가능하다고 설정한다.

+ 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않음
"""

def solution(m, n, puddles):
    MOD = 1_000_000_007
    dp = [[0] * n for _ in range(m)]

    # 시작점 초기화 (시작점은 항상 1개의 경로만 존재함)
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if [i+1, j+1] in puddles:
                dp[i][j] = 0
                continue
            # 위에서 오는 경우
            if i > 0:
                dp[i][j] += dp[i-1][j]
            # 왼쪽에서 오는 경우
            if j > 0:
                dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1] % MOD

m = 4
n = 3
puddles = [[2,2]]

print(solution(m, n, puddles))

def solution(m, n, puddles):
    MOD = 1_000_000_007  # 나눌 수
    dp = [[0] * (n+1) for _ in range(m+1)]  # dp 테이블 초기화, 인덱스를 1부터 시작하기 위해 +1

    # 시작점 초기화
    dp[1][1] = 1

    # 물웅덩이 위치를 set으로 변환, 좌표계 조정
    puddles_set = {(x, y) for x, y in puddles}

    for i in range(1, m+1):
        for j in range(1, n+1):
            # 시작점이거나 물웅덩이인 경우 스킵
            if (i, j) == (1, 1) or (i, j) in puddles_set:
                continue

            # 왼쪽과 위쪽에서 오는 경로의 수를 더함
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    return dp[m][n]