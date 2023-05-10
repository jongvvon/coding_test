# There is 4x4 space that is divided 1x1 square.
# each squrae in space express (x, y) coordinate.
# x is row, y is column.
# Each cell has a number and sight direction.
# number is 1~16 that is not duplicate, 
# sight direction is 1~8 that is four direction and diagonal direction.
# sight direction 1 ~ 8 mean ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# lotate direction is 45 degree. That is sight direction plus 1.

   
# 청소년 상어 - BOJ 19236
# DFS+구현

'''
금일 코테 인증 23.04.27

관련 문제 <백준 19236: 청소년상어> 성공

문제 요약
4x4 크기의 공간, 공간의 각 칸 = (x, y), 한 칸에는 물고기 한 마리, 물고기는 번호와 방향 존재, 1<=번호<=16, 8가지 방향
청소년 상어는 (0,0)을 먹고 들어감, 
이후 물고기 이동
물고기는 번호가 작은 순서부터 이동, 한 칸 이동 가능, 빈 칸과 다른 물고기가 있는 칸만 가능
각 물고기는 방향이 이동할 수 있는 칸을 향할 때 까지 45도 반시계 회전, 다른 물고기가 있을 경우 위치 교환
이후 상어 이동
한 번에 여러개의 칸 이동 가능, 물고기가 있는 칸으로 이동했을 경우 물고기를 먹고
그 방향을 가지게 됨, 이동하는 중에 지나가는 칸의 물고기는 먹지 않음
이후 반복
상어가 먹을 수 있는 물고기 번호의 최대값은?

해결 방법 및 추가 정보
dfs를 이용하여 해결하였다. 한번에 한 동작씩 실행되다보니 dfs를 선택했는데(결국 가장 깊은 depth까지 도달해야하므로)
dfs의 경우 재귀 방법만 기억하면 됐지만 대부분의 높은 난이도 dfs 문제들은 최종적으로 최대값이나 최소값을 얻기를 원하므로
board를 deep copy 하여 분리시켜 재귀를 진행시켰다. 해당 문제의 경우 상어가 움직일 수 있는 모든 방향의 dfs를 실행하면서 쌓이는 점수값에 대하여 최대값만을 저장해주었다.
'''

import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    # 입력시 번호, 방향
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향 - 입력한 리스트대로 0,1 / 2,3 / 4,5 / 6,7
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish


max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    # 4X4 로 고정된 borad 이기 때문에 16회 최대 실행
    for f in range(1, 17):
        f_x, f_y = -1, -1
        # 전체 순회
        for x in range(4):
            for y in range(4):
                # 1부터 16까지 물고기 위치 f_x, f_y 에 저장
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        # 
        f_d = board[f_x][f_y][1]

        # 8방향 회전
        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)

