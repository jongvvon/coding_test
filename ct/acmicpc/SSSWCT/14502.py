import sys
import copy
from collections import deque
from pprint import pprint
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
result = 0

def bfs():
    global result
    # copy to board, because board will be changed by wall function
    c_board = copy.deepcopy(board)
    
    width = 0
    arr = []

    # save virus position
    for i in range(n):
        for j in range(m):
            if c_board[i][j] == 2:
                arr.append([i, j])

    # bfs, find virus and spread
    while arr:
        x, y = arr[0][0], arr[0][1]
        del arr[0]
        for dx, dy in move:
            cx, cy = x + dx, y + dy
            if 0 <= cx and cx < n and 0 <= cy and cy < m:
                if c_board[cx][cy] == 0:
                    c_board[cx][cy] = 2
                    arr.append([cx, cy])
    
    # count safe area
    for i in c_board:
        for j in i:
            if j == 0:
                width += 1

    result = max(result, width)
        
def wall(count):
    if count == 3:
        bfs()
        return

    # recursive 를 이용하여 벽을 세우는 모든 경우의 수를 구함
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(count + 1)
                board[i][j] = 0

wall(0)
print(result)