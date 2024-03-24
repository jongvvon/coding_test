"""
모든 집들은 원형으로 이어져 있음
인접한 두 집을 털면 경보가 울림 -> 즉 인접하지 않은 집들을 털어서 최대의 값을 벌어야함
각 집에 있는 돈이 담긴 배열 money가 주어질 때, 훔칠 수 있는 돈의 최댓값

ex)
money = [1, 2, 3, 1]
return = 4
"""

def solution(money):
    n = len(money)

    # 첫 번째 집을 털 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, n-1):  # 마지막 집을 털 수 없으므로 n-1까지 반복
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 첫 번째 집을 털지 않는 경우
    dp2 = [0] * n
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    # 두 경우 중 최댓값 반환
    return max(dp1[n-2], dp2[n-1])

# 예시 사용
money = [1, 2, 3, 1]
print(solution(money))  # 출력: 4
