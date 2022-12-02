def lottery(depth, n, m):
    if depth == m:
        print(*answer)
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            lottery(depth+1, n, m)
            visited[i] = False
            answer.pop()


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    K = nums[0]
    S = nums[1:]
    visited = [False] * K
    answer = []
