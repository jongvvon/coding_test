"""
네트워크 : 상호 간에 정보를 교환할 수 있도록 '연결'된 형태
간접적으로라도 연결되어 있다면 하나의 네트워크로 판단

n = 컴퓨터의 개수
computers = 연결에 대한 정보가 담긴 2차원 배열

-> 각 컴퓨터를 노드로 하고 간선을 연결하여 네트워크 개수 파악(DFS/BFS 모두 이용 가능)

두 알고리즘 모두 모든 노드를 방문하고 각 연결 요소를 정확히 한 번씩만 탐색하기 때문에, 전체적인 시간 복잡도는 동일하게 (O(N^2))입니다(여기서 (N)은 컴퓨터의 개수입니다).

성능 측면에서는 두 알고리즘 간에 큰 차이가 없으나, 사용하는 자료구조의 차이로 인해 메모리 사용량에서 약간의 차이가 발생할 수 있습니다. 예를 들어, 넓은 그래프에서는 BFS가 사용하는 큐가 매우 커질 수 있고, 깊은 그래프에서는 DFS의 스택(또는 재귀 호출 스택)이 커질 수 있습니다.


"""
from collections import deque


def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if not visited[j]:
            visited[j] = True
            for i in range(len(computers)):
                if computers[j][i] == 1 and not visited[i]:
                    stack.append(i)


def bfs(computers, visited, start):
    queue = deque([start])
    while queue:
        j = queue.popleft()
        if not visited[j]:
            visited[j] = True
            for i in range(len(computers)):
                if computers[j][i] == 1 and not visited[i]:
                    queue.append(j)


def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            # bfs(computers, visited, i)
            answer += 1
    return answer


n = 3
computers = [[1,1,0], [1,1,0], [0,0,1]]
print(solution(n, computers))