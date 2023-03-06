import sys
input = sys.stdin.readline

num = int(input())
array = [0] * (num + 1)
for i in range(1, num + 1):
    array[i] = int(input())

dp = [[0 for _ in range(3)] for _ in range(num + 1)]
dp[1][1] = dp[1][2] = array[1]
# i 번째 계단에 대한 상태는 이전 계단에서 1칸 올라왔는지 2칸 올라왔는지 알면 결정됨.
for i in range(2, num + 1):
    dp[i][1] = dp[i-1][2] + array[i]
    # i 번째 계단에 (1: 한 칸)을 올라옴 -> 그렇기 위해선 이전 단계에서 2칸을 올라온 경우에만 가능
    # 즉, dp[i][1]: i번째 상태에 한칸으로 올라왔다는 것은, 
    # dp[i-1][2]: i-1 번째 상태에 두칸을 올라온 경우에만 가능
    dp[i][2] = max(dp[i-2][1], dp[i-2][2]) + array[i]
    # i 번째 계단에 (2: 두 칸)을 올라옴 -> 두 칸을 올라오기 위해서 이전 상태는 모두 가능
    # dp[i][2]: i번째 상타에 두칸으로 올라옴
    # max(dp[i-2][1], dp[i-2][2]): 최대값을 얻는 것이기 때문에 둘 중 max값으로 접근

print(array)
print(dp)
print(max(dp[-1]))
#commit test