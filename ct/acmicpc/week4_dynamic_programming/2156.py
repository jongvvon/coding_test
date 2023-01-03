n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
dp = [0]  # dp
mdp = [0]  # dp들의 최댓값을 저장하는 mdp

if n >= 1:
    dp.append(wines[1])
    mdp.append(wines[1])
if n >= 2:
    dp.append(wines[1] + wines[2])
    mdp.append(wines[1] + wines[2])
    # 우선, dp와 mdp를 채워놓고 시작

for i in range(3, n + 1):
    temp1 = wines[i] + wines[i - 1] + mdp[i - 3]
    temp2 = wines[i] + mdp[i - 2]
    dp.append(max(temp1, temp2))  # dp값을 갱신
    mdp.append(max(dp))  # mdp에 dp 배열의 최댓값을 입력
    # 말씀하신 바와 같이 mdp가 이미 그 값을 기억하므로 안 마신 경우를 생각할 필요가 없음!
print(max(mdp))
