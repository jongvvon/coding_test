# 10026 적록색약
# 그리드의 크기 = N x N
# R, G, B 로 이루어진 그림이 있다.
# 그림은 몇 개의 구역으로 나누어져 있으며 같은 색으로 이루어져 있음
# 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
# 그림이 입력으로 이루어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램
# 적록색약이 아닌 사람 : R - G - B
# 적록색약 : R&G - B
# 해당 기준으로 구역을 구분하여 구역의 수 출력
from collections import deque

move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

n = int(input())

drawing = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = 0

def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in move:
                cx, cy = x + dx, y + dy
                if 0 <= cx and cx < n and 0 <= cy and cy < n:
                    if drawing[cx][cy] == color:
                        q.append([cx, cy])

# normal
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = drawing[i][j]
            bfs(i, j, color)
            result += 1
print(result, end=" ")


# color weakness drawing
visited = [[False] * n for _ in range(n)]
result = 0
# drawing color change for color weakness
for i in range(n):
    for j in range(n):
        if drawing[i][j] == 'G':
            drawing[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = drawing[i][j]
            bfs(i, j, color)
            result += 1
print(result)

"""
일반적인 다른 BFS 탐색과 다른 점은 그래프 내에서 이동할 수 있는 조건이 3개라는 점이다.
따라서 bfs parameter로 color를 추가하여 그래프의 해당 값을 color와 비교해 같은 값이면 이동할 수 있고
다르면 이동할 수 없도록 처리한다.
color weakness 의 경우 'G' 'R' 을 같은 것으로 처리해주어야 하므로 두 가지의 방법이 존재한다.
1. graph 자체의 속성을 변경하는 방법
2. bfs 자체의 조건을 바꿔주는 방법

1-> graph 자체의 속성을 변경하게 될 경우
일반 / 색약 나누어 bfs 를 진행해야 하며
진행 방식에 대해서 고민해봐야 될 것으로 보임
다른 case 의 경우 특정 숫자 혹은 문자 한가지만을
체크하여 bfs 를 진행하면 됐지만 
해당 문제의 경우 3가지/2가지의 타겟이 존재하므로
그 타겟의 속성을 인자로 전달하여
해결해야할 것으로 보임

그래프를 복사해야 하는가 ?
"""
