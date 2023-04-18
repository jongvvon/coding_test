'''
금일 코테 인증 23.04.18

관련 문제 <백준 4963: DFS/BFS> (완료)

문제 요약
가로, 세로, 대각으로 이루어진 섬의 경우 하나로 계산하고 전체 그래프에서 섬의 개수 출력 프로그램

해결 방법 및 추가 정보
가로 / 세로 / 대각 이동이라는 점에서 평소에 move 리스트보다 2배를 사용하게 된다.
문제의 경우 연결된 노드를 한번씩 방문하면서 visited 처리를 해주었고 이를 위해 bfs를 사용하였다.

문제는 어려운 편은 아니였지만 배열 기준으로 시계방향으로 8방향을 12시부터 선정했는데
배열의 경우 2차원 그래프와는 다르게 생각해야하며 여기서 실수를 해 시간을 조금 잡아먹혔다.

'''
from collections import deque

moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    global count
    while q:
        cx, cy = q.popleft()
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx and nx < h and 0 <= ny and ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[cx][cy] = True
                    visited[nx][ny] = True
    


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    count = 0
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i, j, visited)
                count += 1

    print(count)


