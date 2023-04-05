import sys
from collections import deque
input = sys.stdin.readline

# 바이러스를 막기 위한 벽 세우기
# 연구소의 크기 = N x M 직사각형
# 직사각형은 1x1 크기의 정사각형으로 나누어져 있음
# 세로 새울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 함
# 0: 빈 칸, 1: 벽, 2: 바이러스
# 벽 3개를 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역
# 안전 영역의 최대값을 구하는 프로그램
# INPUT: N, M, map

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

infect = []
def infectious():
    for i in range(n):
        for j in range(m):
            if board[i][j] == '2':
                infect.append([i, j])
    
    for ix, iy in infect:
        for dx, dy in move:
            iix, iiy = ix+dx, iy+dy
            if 0 < iix <= m and 0 < iiy <= n and board[iix][iiy] != 0:
                board[iix][iiy] = 2


def bfs(x, y):
    visted = []
    q = deque()
    for dx, dy in move:
        q.append([x + dx, y + dy])

    ddx, ddy = q.popleft()
    while q:
        if 0 < ddx <= n and 0 < ddy <= m:
            visted[ddx][ddy] = 0

