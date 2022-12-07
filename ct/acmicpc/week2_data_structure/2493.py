num = int(input())
tower = list(map(int, input().split()))

stack = []
answer = [0 for _ in range(num)]

for i in range(num):
    while stack:
        if stack[-1][1] > tower[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tower[i]])

print(*answer)

