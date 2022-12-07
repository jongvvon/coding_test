array = input()
stack = []
cnt = 0
i = 1
flag = True
while flag:
    if i-1 == len(array):
        flag = False
        break
    if array[i-1] == '(' and array[i] == ')':
        cnt += len(stack)
        i += 2
    elif array[i-1] == '(':
        stack.append(i-1)
        i += 1
    elif array[i-1] == ')':
        stack.pop()
        cnt += 1
        i += 1

print(cnt)

