student = [0] * 31
for _ in range(0, 28):
    student[int(input())] = 1
ans = list(filter(lambda x: student[x] == 0, range(len(student))))
for i in range(1, len(ans)):
    print(ans[i])
