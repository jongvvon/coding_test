N, M = map(int, input().split())
answer = []


def dfs():
    if len(answer) == M:
        print(*answer)
        return
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()


dfs()
