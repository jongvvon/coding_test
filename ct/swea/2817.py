def dfs(idx, x, y):
    global ans

    if y == K:
        ans += 1

    dfs(idx+1, x, y)
    dfs(idx+1, nums[idx], y)



for case in range(1, int(input())+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    print("{} {}".format(case, ans))
