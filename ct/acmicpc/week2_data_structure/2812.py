N, K = map(int, input().split())
num = input()
stack = []
cnt = 0
i = 0

while True:
    if len(stack) == N - K:
        break
    stack.append(int(num[i]))
    if cnt < K:
        while stack:
            if stack[-1] < int(num[i+1]):
                stack.pop()
                cnt += 1
                if cnt == K:
                    break
            else:
                break
    i += 1

for j in stack:
    print(j, end="")