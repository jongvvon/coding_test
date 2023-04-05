# N x N 크기의 공간에 물고기 M 마리, 아기상어 1마리
# 공간은 1 x 1 크기의 정사각형으로 나누어짐
# 물고기의 크기는 자연수로 표현되며 아기 상어의 경우 크기가 2이며 1초에 인접 상하좌우로 한칸 씩 이동
# 물고기가 공간에 없다면 엄마 상어에게 도움을 요청함
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이 동할 때, 지나야 하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정
# 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동 했다면, 이동과 동시에 물고기를 먹는다.
# 자신과 크기와 "같은 수" 물고기를 먹을 때 마다 크기가 1씩 증가한다.
# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램
# "자신의 크기보다 작은 물고기만 먹을 수 있으며 자신의 크기만큼 개수의 물고기를 먹게되면 크기가 1 증가"

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for i in range(n):
    for j in range(n):
        # location of baby shark
        if board[i][j] == 9:
            # shark = [x, y, size, eat]
            shark = [i, j, 2, 0]
            # remove baby shark
            board[i][j] = 0


def bfs():
    vistied = []
    q = deque()
    q.append([shark[0], shark[1], 0])
    vistied.append([shark[0], shark[1]])
    while q:
        x, y, cnt = q.popleft()
        if cnt > 0:
            return x, y, cnt
        # move baby shark
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            # check if shark can move
            # location is in board and location is smaller than shark's size
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] <= shark[2] and [nx, ny] not in vistied:
                q.append([nx, ny, cnt + 1])
                vistied.append([nx, ny])
                # check if shark can eat
                if board[nx][ny] != 0 and board[nx][ny] < shark[2]:
                    return nx, ny, cnt + 1
                
time = 0
while True:
    x, y, cnt = bfs()
    # if shark can't move
    if cnt == 0:
        break
    # shark eat fish
    board[x][y] = 0
    shark[3] += 1
    # shark grow up
    if shark[3] == shark[2]:
        shark[2] += 1
        shark[3] = 0
    shark[0], shark[1] = x, y
    time += cnt

print(time)