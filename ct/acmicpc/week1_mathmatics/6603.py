def combine(idx, x):
    if idx == R:
        print(*result)
        return
    for i in range(x, K):
        result[idx] = S[i]
        print(idx, result)
        combine(idx+1, i+1)


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    K = nums[0]
    S = nums[1:]
    R = 6
    result = [0] * R
    combine(0, 0)
    print()
