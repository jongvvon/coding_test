from pprint import pprint

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

pprint(board)

# 최대 5회 이동, 상하좌우, 끝까지
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def move(x, y, dx, dy):
    nx, ny = x, y
    