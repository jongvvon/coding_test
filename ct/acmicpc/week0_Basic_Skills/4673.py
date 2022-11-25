num = set(range(1, 10001))
ans = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    ans.add(i)

self_num = sorted(num - ans)
for i in self_num:
    print(i)

