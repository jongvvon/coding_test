from collections import deque

move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
result = 0

# 1 끼리 붙어있는 componant 개수를 구하라?
def bfs(graph, x, y):
    global result
    q = deque()
    # 배추 위치 저장
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            cx, cy = x + dx, y + dy
            if 0 <= cx and cx < n and 0 <= cy and cy < m:
                if graph[cx][cy] == 1:
                    graph[cx][cy] = 0
                    q.append([cx, cy])
    return


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                result += 1
    print(result)
    result = 0