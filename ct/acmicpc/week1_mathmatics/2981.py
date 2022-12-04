# 유클리드 호제법
# num of wrote numbers in paper
import math


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


N = int(input())
nums = sorted([int(input()) for _ in range(N)])

temp = []
for i in range(1, N):
    temp.append(nums[i] - nums[i-1])

gcd_num = temp[0]
for j in range(1, len(temp)):
    gcd_num = GCD(gcd_num, temp[j])

result = set()
for k in range(2, int(math.sqrt(gcd_num)) + 1):
    if gcd_num % k == 0:
        result.add(k)
        result.add(gcd_num // k)
result.add(gcd_num)
print(*sorted(list(result)))

# min(nums)가 10억이 될 수 있음 -> 시간 초과
# for i in range(2, min(nums)+1):
#     for j in nums:
#         temp.append(j % i)
#     if max(temp) == min(temp):
#         print(i, end=" ")
#     temp = []
