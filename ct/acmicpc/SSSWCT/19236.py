# There is 4x4 space that is divided 1x1 square.
# each squrae in space express (x, y) coordinate.
# x is row, y is column.
# Each cell has a number and sight direction.
# number is 1~16 that is not duplicate, 
# sight direction is 1~8 that is four direction and diagonal direction.
# sight direction 1 ~ 8 mean ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# lotate direction is 45 degree. That is sight direction plus 1.

import sys
import copy
from pprint import pprint

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

fish = []
for i in range(4):
    for j in range(4):
        fish.append([board[i][2*j], board[i][2*j+1]])
board = copy.deepcopy(fish)

result = 0

def dfs(x, y, d, score, board):
    global result
    