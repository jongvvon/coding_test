N, S = map(int, input().split())
nums = list(map(int, input().split()))


def dfs(idx, x):
    global cnt
    if idx >= N:
        return
    x += nums[idx]
    if x == S:
        cnt += 1

    dfs(idx+1, x)
    dfs(idx+1, x-nums[idx])


cnt = 0
dfs(0, 0)
print(cnt)
