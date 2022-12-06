stack = []
answer = []
flag = True
n = 1
for case in range(int(input())):
    num = int(input())
    while n <= num:
        stack.append(n)
        answer.append("+")
        n += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")

    else:
        print("NO")
        flag = False
        break

if flag:
    for i in answer:
        print(i)
