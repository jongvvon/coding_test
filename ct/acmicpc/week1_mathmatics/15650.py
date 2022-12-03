N, M = map(int, input().split())
answer = []


def dfs(num):
    if len(answer) == M:
        print(*answer)
        return

    for i in range(num+1, N+1):
        answer.append(i)
        dfs(i)
        answer.pop()


dfs(0)
