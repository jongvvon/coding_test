# 모든 경로에 대한 값을 더하여 최솟값을 결정해라.


from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_count = 0

def bfs(i, j, board, visited, cnt):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == False:
                cnt += board[nx][ny]
                if nx == n-1 and ny == n-1:
                    return cnt
                q.append((nx, ny))
                visited[nx][ny] = True
                bfs(nx, ny, board, visited, cnt)
            


while True:
    n = int(input())
    if not n:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    print(board, visited)
    print(bfs(0, 0, board, visited, board[0][0]))