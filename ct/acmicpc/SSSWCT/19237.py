'''
금일 코테 인증 23.05.02

관련 문제 <백준 19237: 어른상어> 성공

문제 요약
N x N 공간, 상어만 존재, 1부터 M 이하의 자연수 보유, 상어는 다른 상어를 쫓아내며, 작은 번호일 수록 강함
최초, 모든 상어는 자신의 위치에 냄새를 뿌림
1초마다, 모든 상어가 동시에 상하좌우 인접한 칸중 하나로 이동 후 냄새 뿌림
k번 이동하고 나면 냄새는 사라짐
상어의 이동방향은 먼저 인접한 칸중 아무 냄새가 없는 칸, 없다면 자신의 냄새
이동 가능한 칸이 여러개라면 특정한 우선 순위를 따름
상어마다 다를 수 있고, 같은 상어라도 보고 있는 방향에 따라 다름
맨처음 바라보는 방향이 주어지고 그 이후에는 이동한 방향이 보고 있는 방향
입력으로 N, M, k 그리고 graph 와 우선순위가 주어진다.
출력으로는 1번 상어만 남게되는 시간을 구한다

해결 방법 및 추가 정보
진짜 어려웠던 문제였다. dfs를 활용하였으며 맵과 방향, 우선순위를 저장해준뒤
다른 dfs와 동일하게 진행하였으며 주변 이동 가능한 경우와 못하는 경우(자신의 냄새로 이동해야하는 경우)의 조건과
우선 순위에 따른 조건 또한 연결시켜 해결하였다.
3주만에 다시 풀어봤지만 여전히 너무 고민을 많이 하게 하는 문제였던 것 같다.
'''


n, m, k = map(int, input().split())

# 처음상어 위치
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


shark = [[0,0] for _ in range(m)]

# 상어의 초기 방향 정해주기
directions = list(map(int, input().split()))

# 상어의 방향별 우선순위 받아오기(위 아래 왼쪽 오른쪽)
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상황판 그리기(상어번호, 냄새가 머무는 시간, 방향)
smell = [[[0, 0]] * n for _ in range(n)]

# 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 남아있는 경우
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 위치의 경우
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]


# 상어 이동
def move():
    new_data = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                direction = directions[data[x][y] - 1]
                found = False
                # 상어의 위치인 경우
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 나지 않는 곳이라면
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else :
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True
                            break
                if found:
                    continue

                # 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == data[x][y]: # 자신의 냄새가 있는 곳이라면
                            # 해당 상어 방향 변경
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

answer = 0
while True:
    update_smell()
    new_data = move()
    data = new_data
    answer += 1

    check = True
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if answer >= 1000:
        print(-1)
        break