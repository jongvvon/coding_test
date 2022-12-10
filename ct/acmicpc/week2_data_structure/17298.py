num = int(input())
array = list(map(int, input().split()))
stack = []
answer = [-1] * num

for i in range(num-1):
    stack.append(i)
    if array[stack[-1]] < array[i+1]:
        while stack:
            if array[stack[-1]] < array[i+1]:
                answer[stack.pop()] = array[i+1]
            else:
                break

print(*answer)
