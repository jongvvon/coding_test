'''
금일 코테 인증 23.05.03

관련 문제 <백준 5567: 결혼식> 성공

문제 요약
tree 구조를 입력받아 dfs/bfs 이용하여 linked 관계에 따라 결과를 출력하라

해결 방법 및 추가 정보
n x m 형식의 그래프 문제뿐 아니라 tree 구조로 링크 관계를 입력으로 주어지는 문제들도 있는데
해당 문제의 감을 익히기 위해 풀어본 문제이다.
알고리즘 작동 원리를 이해했다면 쉽게 넘어갈 수 있을 것이라고 생각된다.
'''
from collections import deque, defaultdict

def bfs(num):
    cnt = 0
    visited = [False for _ in range(n+1)]
    visited[num] = True

    q = deque()
    q.append([num, 0])
    while q:
        u, dist = q.popleft()
        if dist <= 2:
            cnt += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = 1
                q.append([v, dist+1])

    return cnt-1    


n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
