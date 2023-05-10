"""

"""

from collections import deque

num_of_computer = int(input())
num_of_pair = int(input())

graph = [[] for _ in range(num_of_computer + 1)]

count = 0
for _ in range(num_of_pair):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (num_of_computer + 1)
def bfs(v):
    global count
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count += 1
                bfs(i)


bfs(1)

print(count)