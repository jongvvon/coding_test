N = input()
N = list(N)
M = int(input())

idx = len(N)
for _ in range(M):
    order = list(map(str, input().split()))

    if order[0] == 'P':
        N.insert(idx, order[1])
        idx += 1

    if order[0] == 'L':
        if idx != 0:
            idx -= 1

    if order[0] == 'D':
        if idx != len(N) - 1:
            idx += 1

    if order[0] == 'B':
        if idx != 0:
            N.remove(N[idx-1])
            idx -= 1

print("".join(N))
