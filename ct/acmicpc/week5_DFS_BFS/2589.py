'''
금일 코테 인증 23.04.13

관련 문제 <백준 2589> (완료) - pypy

문제 요약
육지는 'L' 바다는 'W'로 표시된 graph, 상하좌우로 이웃한 육지로 이동가능하며, 한 칸 이동 시 한시간 소요
보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있음
두 곳 사이를 최단 거리로 이동하기 위해서는 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안됨
즉, L과 L 사이에 최단 거리들 중 가장 긴 시간이 걸리는 L 들을 찾아 그 시간을 출력

해결 방법 및 추가 정보
삼성 코테 준비 기간동안 유사한 문제를 많이 풀었어서 그런지 문제 접근 및 코드 작성은 쉬운 편이였다.
최단 경로를 찾아내는 문제기 때문에 bfs를 이용했으며 모든 'L' 즉, 육지에서의 최단 경로와 거리를 계산해준 뒤
최대값을 출력하는 방식으로 해결하였다.
해당 문제의 경우 바로 인접한 육지 2개만을 계산해야 되는 상황에서 한번만 이동하면 되는 경우에 첫 좌표의
방문처리를 안하게 되면 거리가 1이 아닌 2로 나오는 문제가 있었는데 이를 해결하기 위해 처음 bfs 가 실행 될때
첫 좌표의 방문 처리를 했으나 그렇게 되면 동서남북으로의 진행이 막히는 상황이 발생했고
이를 위해 이동한 좌표가 유용할 경우 본인의 좌표를 방문처리 하는 것으로 해결했다.
설명만으로는 이해가 힘든 표현일 수 있으나 직접 문제를 겪게된다면 도움이 될 것으로 생각된다.

'''
from pprint import pprint
from collections import deque

# West, East, North, South
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

row, col = map(int, input().split())

graph = [list(map(str, input())) for _ in range(row)]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[False for _ in range(col)] for _ in range(row)]
    timer = [[0 for _ in range(col)] for _ in range(row)]

    while q:
        rx, ry = q.popleft()
        for dx, dy in moves:
            # visited[dx][dy] = True
            cx, cy = rx + dx, ry + dy
            if 0 <= cx and cx < row and 0 <= cy and cy < col:
                if graph[cx][cy] == 'L' and visited[cx][cy] == False:
                    timer[cx][cy] = timer[rx][ry] + 1
                    visited[rx][ry] = True
                    visited[cx][cy] = True
                    q.append((cx, cy))

    return timer

result = []

for i in range(row):
    for j in range(col):
        if graph[i][j] == 'L':
            temp = bfs(i, j)
            result.append(max(map(max, temp)))
        

print(max(result))