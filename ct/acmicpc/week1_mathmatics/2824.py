import math

N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))
N_num, M_num = 1, 1

for i in N_nums:
    N_num *= i
for j in M_nums:
    M_num *= j

ans = math.gcd(N_num, M_num)
ans = str(ans)

if len(ans) > 9:
    print(ans[len(ans)-9:])
else:
    print(ans)