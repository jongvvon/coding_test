from pprint import pprint

n, m = map(int,input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(str, input())))

# print(MAP)

for r in range(n):
    for c in range(m):
        if MAP[r][c] == 'R':
            # 빨간 구슬 시작 위치
            rsx, rsy = r, c
        if MAP[r][c] == 'B':
            # 파랑 구슬 시작 위치
            bsx, bsy = r, c
        if MAP[r][c] == 'O':
            # 구멍 위치(변동 없음)
            ox, oy = r, c

# x, y - 좌표 / dx, dy - directions x, y
def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    # 상하좌우로 기울일 수 있으며 해당 동작 수행 시, 
    # 구슬은 벽 혹은 구멍까지 이동 가능
    while MAP[nx + dx][ny + dy] != '#' and MAP[nx][ny] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt

# print(MAP)            

def solution():
    visited = {}
    # 아래, 위, 좌, 우
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    visited[(rsx,rsy)] = 1
    s = [[rsx,rsy,bsx,bsy,0]]

    while s:
        pprint(MAP)
        pprint(s)
        pprint(visited)
        rx, ry, bx, by, cnt = s.pop(0)
        # 10번 이하로 움직여야함, 아닐 시 -1 출력
        if cnt >= 10:
            return -1

        # moves 배열 순서대로 공 이동
        for dx, dy in moves:
            # 빨간/파란 구슬 이동 후 좌표
            rrx, rry, rcnt = move(rx,ry,dx,dy)
            bbx, bby, bcnt = move(bx,by,dx,dy)

            # 파란 구슬 구멍에 빠지지 않았을 때,
            if MAP[bbx][bby] != 'O':
                # 빨간 구슬이 구멍에 들어왔다면, 
                # moves에서 count한 횟수 + 1 출력후 while문 종료
                if rrx == ox and rry == oy:
                    return cnt + 1
                # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 때
                if rrx == bbx and rry == bby:
                    # rcnt > bcnt : 빨간 구슬의 이동 횟수가 더 많으므로
                    # 좌표를 -(dx, dy)만큼 조정해준다.
                    if rcnt > bcnt:
                        rrx, rry = rrx-dx, rry-dy
                    else:
                        bbx, bby = bbx-dx, bby-dy
                
                # 이미 존재하던 map이라면 무시하고 진행
                if (rrx,rry,bbx,bby) in visited:
                    continue

                else:
                    # 기 존재하는 map과 구슬의 좌표가 아닐 시, visited에 적용
                    visited[(rrx,rry,bbx,bby)] = 1
                    # 이동한 좌표로 최신화
                    s.append([rrx,rry,bbx,bby,cnt+1])
                    # print("방문처리 : ", rrx, rry, bbx, bby, cnt+1)
    # 예외처리
    return -1

print(solution())