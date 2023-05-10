"""
금일 코테 인증 23.05.09

관련 문제 <백준 2512: 예산> (완료)

문제 요약
정해진 총액 이하에서 가능한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
모든 요청이 배정될 수 없는 경우 특정한 정수 상한액을 계산, 그 이상인 예산 요청에는 모두 상한액 배정, 이하인 경우 그대로 배정

해결 방법 및 추가 정보
binary search 공부할 겸 풀어본 문제, 이진 탐색 / 이분 탐색의 경우 중간 값을 정해주고 재귀 형식을 통해
특정한 값들을 중간값과 비교하여 이상 / 이하 처럼 두 가지 범위로 search 하는 방법이다.
해당 문제의 경우에는 상한액을 찾는 문제인데 예상 상한액을 비교한 뒤 위 문제 요약에 따른 조건에 맞춰서
값을 비교하며 업데이트 하는 형식으로 해결하였다.
"""


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 0, max(arr)
# binary search
while start <= end:
    # upper limit
    mid = (start + end) // 2
    curr = 0
    # i is required cost
    for i in arr:
        if i >= mid:
            curr += mid
        else:
            curr += i
    if curr <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)