n = int(input())
price = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + price[j])
print(dp[-1])

'''
카드팩의 종류는 카드 1개가 포함된 카드팩, ... , n개가 포함된 카드팩까지 n개 존재
카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것
돈을 최대한 많이 지불해서 카드 N개를 구매하려고 함
카드가 i개 포함된 카드팩의 가격은 price[i]

max(price) = 
price[1] + dp[i-1],
price[2] + dp[i-2],
price[3] + dp[i-3],
...
price[i] + dp[0]



=> dp[i] = price[j] + dp[i-j]

'''