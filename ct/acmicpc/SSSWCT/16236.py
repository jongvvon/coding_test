'''
금일 코테 인증 23.04.21

관련 문제 <백준 16236: 아기상어> 성공

문제 요약
N x N 크기의 map, 물고기 m 마리와 아기 상어 1마리 모두 크기를 가지고 있음
아기 상어는 1초에 상하좌우로 이동하고 자신의 크기보다 큰 물고기가 있는 칸은 못 지나가며 나머지 칸은 이동 가능
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있고 크기가 같은 물고기는 먹지 못하지만 지나갈 수 있음
더 이상 먹을 수 있는 물고기가 없다면(= map안에 자신의 크기보다 작은 물고기가 없음) 엄마 상어에게 도움 요청
먹을 수 있는 물고기가 1마리보다 많다면 거리가 가장 가까운 물고기 우선
거리는 지나야하는 칸의 개수의 최솟값, 가까운 물고기가 많다면 가장 위 우선 그것도 많다면 가장 왼쪽 우선
이동은 1초 먹는데 걸리는 시간은 없음
자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는가?

해결 방법 및 추가 정보
bfs를 이용하였으며 방문 여부 외에도 거리를 list 인자로 입력하며 진행하였다. 아기 상어의 위치를 queue에 저장하는 형식으로 진행했으며
상하좌우 이동 시 먹을 수 있는 물고기들의 우선 순위를 lambda를 이용하여 return 해주고 상어 위치를 계속 업데이트 해주었다.
움직이는 시간은 곧 거리이며 더 이상 먹을 수 있는 물고기가 없는 상태일 경우 종료시켜주었다.
코드의 경우 생각보다 간단하게 구현됐지만 이동하면서 거리를 저장한다는 점과 주변에 가까운 물고기가 많은 경우 priority를 정해주는 곳에서
고민을 많이하게한 문제였다. 'sorted(temp, key=lambda x: (-x[2],-x[0],-x[1]))' 해당 코드의 동작 방식은 계속해서 기억을 해두는 것이
효율적인 python 코드 작성에 도움이 될 것으로 보인다.
'''

import sys
from collections import deque

input = sys.stdin.readline

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

# moves 배열과 동일
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
x, y, size = 0, 0, 2
# 상어위치 save
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def biteFish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
    q = deque()
    # 현재 아기 상어의 위치 queue에 저장
    q.append((x,y))
    visited[x][y] = 1
    temp = []
    while q:
        # currennt x, y: 현재 아기 상어의 위치
        cur_x, cur_y = q.popleft()
        # 동서남북 방향으로 한번씩 진행
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # n is limited of map
            # 현재 아기 상어의 위치가 map 안에 존재하며 방문하지 않은 좌표 일 시,
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 해당 좌표의 값(fish_size) <= shark_size
                if graph[nx][ny] <= shark_size:
                    # 현재 좌표 저장
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    # 현재좌표의 거리는 이전 좌표의 거리 + 1
                    # 즉, 지나온 거리 + 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    # 상하좌우의 있는 물고기가 만약 shark size 보다 작고 해당 그래프가 0이 아니라면 그 값을 temp에 저장한다.
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))

# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# temp에 저장된 값 = 특정 좌표 기준으로 동서남북 중 하나에 있는 물고기가 먹을 수 있는 상태임
    return sorted(temp, key=lambda x: (-x[2],-x[0],-x[1]))


cnt = 0
result = 0
while 1:
    shark = biteFish(x, y, size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(shark) == 0:
        break
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영해준다.
    nx, ny, dist = shark.pop()
    
    #움직이는 칸수가 곧 시간이 된다.
    result += dist
    graph[x][y], graph[nx][ny] = 0, 0
    #상어좌표를 먹은 물고기 좌표로 옮겨준다.
    x,y = nx,ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(result)

