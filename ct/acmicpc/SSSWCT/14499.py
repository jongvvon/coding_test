# Grid : N x M / loc of dice : (x, y) / num of order : k
n, m, x, y, k = map(int, input().split())

# right = east, up = north
# coordinate of map : (r, c) / r is far from north, c is far from west
map_of_dice = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0] * 6
move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # East
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: # West
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: # North
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else: # South
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx, ny = x, y
for i in order:
    dx, dy = move[i]
    nx += dx
    ny += dy

    if 0 > nx or nx >= n or 0 > ny or ny >= m:
        nx -= dx
        ny -= dy
        continue

    turn(i)
    if map_of_dice[nx][ny] == 0:
        map_of_dice[nx][ny] = dice[-1]
    else:
        dice[-1] = map_of_dice[nx][ny]
        map_of_dice[nx][ny] = 0

    print(dice[0])


"""
해당 동작을 수행할때마다 지도에 업데이트가 되는 경우는 쉽지만
현재 주사위의 값을 저장해야할 수단이 필요하다
주사위의 전개도에 따라 1, 2, 3, 4 에 따른 배열이 필요할 것으로 보임
"""