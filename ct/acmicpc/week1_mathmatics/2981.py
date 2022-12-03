# 유클리드 호제법
# num of wrote numbers in paper
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

temp = []
for i in range(N-1):
    temp.append(nums[i+1] - nums[i])


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


gcd_array = []
for j in range(len(temp)):
    gcd_array[i] = GCD(temp[i], i)

# min(nums)가 10억이 될 수 있음 -> 시간 초과
# for i in range(2, min(nums)+1):
#     for j in nums:
#         temp.append(j % i)
#     if max(temp) == min(temp):
#         print(i, end=" ")
#     temp = []
