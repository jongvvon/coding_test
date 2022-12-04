def dfs():
    if len(ans) == N:
        print(*ans)
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()


N = int(input())
ans = []
dfs()