"""
금일 코테 인증 23.05.11

관련 문제 <백준 2468: 안전 영역> (완료)

문제 요약
지역의 높이를 행과 열로 제공하고 물에 잠기는 영역은 정해지지 않았을 때, 안전한 지역이 최대로 몇 군데인지 출력하라

해결 방법 및 추가 정보
문제를 읽자마자 행과 열로 이루어진 graph에서 상하좌우로 이동하며 독립된 componant가 몇개인지 계산하면 된다고 생각했고
개인적으로 사용하기 편한 bfs를 이용하여 풀이를 시작했다. 이 문제에서 또 유심히 봐야할 점은 2부터 100사이의 높이를 가지고 있고
비가 오는 양을 0부터 가장 높은 땅까지 모두 계산하여 안전 지역을 계산 후 최대 값을 출력해야 한다는 점이였다.
"""
from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maxNum = 0

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum: maxNum = graph[i][j]

def bfs(x, y, value, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        rx, ry = q.popleft()

        for dx, dy in moves:
            cx, cy = rx + dx, ry + dy
            if 0 > cx or cx >= n or 0 > cy or cy >= n:
                continue
            if graph[cx][cy] > value and visited[cx][cy] == False:
                visited[cx][cy] = True
                q.append((cx, cy))

result = 0
for i in range(maxNum):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == False:
                bfs(j, k, i, visited)
                count += 1

    if result < count:
        result = count

print(result)
