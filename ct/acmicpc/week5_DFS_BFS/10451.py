"""
금일 코테 인증 23.05.11

관련 문제 <백준 10451: 순열 사이클> (완료)

문제 요약
입력의 순서대로 linked 된 graph를 만들고 componant 의 개수를 구하라!

해결 방법 및 추가 정보
순회하는 graph 의 개수를 구하는 문제이기 때문에 dfs를 이용하였다.
이전에 풀었던 11724와 동일한 동작 방식이였기 때문에 어렵지는 않았고
역시나 u, v 의 tree 구조를 입력 방식에서 변환하는게 중요하다고 느꼈다.

"""

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)

    for i in range(1, n+1):
        graph[i].append(arr[i-1])

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)