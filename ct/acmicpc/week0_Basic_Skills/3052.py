ans = {}
for i in range(10):
    ans[int(input()) % 42] = i

print(len(ans))