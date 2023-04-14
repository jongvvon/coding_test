'''
금일 코테 인증 23.04.14

관련 문제 <백준 16234: 인구 이동> (완료)

문제 요약
N x N 크기의 정사각형에서 r행 c열에 살고 있는 나라에는 A[r][c] 명이 살고 있음
인구 이동 순서
1. 인접한 "두 나라의 인구 차이"가 L명 이상, R명 이하 라면 국경선을 하루 동안 연다.
2. 국경선이 열린 후 인구 이동 시작
3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있다면, 그 나라를 연합이라고 칭함
4. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수), 소수점은 버림
5. 연합 해체 후 국경선 닫음
-> 최종적으로 인구 이동이 며칠동안 발생하는지 구하라

해결 방법 및 추가 정보
bfs 사용하여 동서남북 방향으로 이동이 가능한 조건일 시 인구수를 더해주고 더 이상 움직이지 못하는 경우 연합의 수로 나누어주었다.
이를 위해 union 이라는 리스트를 추가적으로 생성해주었으며 모든 그래프의 완전 탐색을 통하여 해결하였다.
'''
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# bfs를 통해 동서남북으로 진행할 수 있다면 계속 진행하면서 값을 더한 뒤 재분배?
# 완전 탐색이 필요한가? 
# 주변으로 진행할 수 있는 cell인지 판단 후 진행하면 메모리 누수를 막을 수 있는가?
# bfs 에 들어오는 coordinate의 기준이 필요함
# (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 계산 방식 결정 필요
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visitied[x][y] = True
    union = [(x, y)]
    count = graph[x][y]
    while q:
        rx, ry = q.popleft()
        for dx, dy in moves:
            cx, cy = rx + dx, ry + dy
            if 0 <= cx and cx < n and 0 <= cy and cy < n and visitied[cx][cy] == False:
                if l <= abs(graph[rx, ry] - graph[cx, cy]) <= r:
                    union.append((cx, cy))
                    visitied[cx][cy] = True
                    q.append((cx, cy)) 
                    count += graph[cx][cy]
            else:
                continue
    for i, j in union:
        graph[i][j] = count // len(union)
    
    return len(union)


result = 0
while True:
    visitied = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if not visitied[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    
    if not flag:
        break
    result += 1

print(result)