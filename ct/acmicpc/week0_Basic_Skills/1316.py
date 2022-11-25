cnt = 0
for case in range(0, int(input())):
    word = input()
    temp = []
    for i in word:
        if i in temp:
            if temp.pop() != i:
                break
            else:
                temp.append(i)
        temp.append(i)
        if "".join(temp) == word:
            cnt += 1

print(cnt)