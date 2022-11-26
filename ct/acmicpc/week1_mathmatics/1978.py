import math

A = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(len(nums)):
    if nums[i] == 2:
        cnt += 1
    if nums[i] != 1:
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                break
            if nums[i] - 1 == j:
                cnt += 1

print(cnt)