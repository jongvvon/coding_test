from collections import deque

def dfs(graph, root):
    visted = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visted:
            visted.append(n)
            stack += graph[n] - set(visted)
    
    return visted

def bfs(graph, root):
    visted = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visted:
            visted.append(n)
            queue += graph[n] - set(visted)
    
    return visted


graph = {}
# n is number of node
# m is number of edge
# v in start node
n, m, v = map(int, input().split())
for i in range(m):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(graph)