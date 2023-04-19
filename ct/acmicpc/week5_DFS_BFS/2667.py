'''
금일 코테 인증 23.04.19

관련 문제 <백준 2667: 단지번호붙이기> 성공

문제 요약
정사각형 지도 / 1의 경우 집, 0의 경우 공터 / 상하좌우 / 단지수(linked) 출력 및 단지내 집 수 출력

해결 방법 및 추가 정보
동서남북 방향 이동, linked 된 노드의 경우 한 단지 판정, 그 단지 안에서 집의 개수 count
bfs 이용하였고 동서남북으로 돌며 집 탐색 후 집이 있을 경우 방문 처리 및 count += 1
처음에는 return 되는 값이 많아서 set() 을 이용하였으나 단지의 개수가 같을 수도 있다는 전제를 고려하지 않은 탓에 문제가 발생했다.
해결을 위해 bfs 진입점에 추가 조건문을 걸어주고 list로 변경시켜 해결하였다.
'''

from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(i, j):
    count = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
    return count

temp = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            temp.append(bfs(i, j))
            
print(len(temp))
for k in sorted(temp):
    print(k)