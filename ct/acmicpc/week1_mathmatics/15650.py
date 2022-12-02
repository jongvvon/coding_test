def dfs(idx, x):
    if idx == M:
        print(*answer)
        return
    for i in range(x+1, N+1):
        answer.append(i)
        dfs(idx+1, i)
        answer.pop()


N, M = map(int, input().split())
answer = []
dfs(0, 0)
