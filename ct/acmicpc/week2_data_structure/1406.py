import sys
input = sys.stdin.readline

N = input().rstrip()
N = list(N)
N_tmp = []

idx = len(N)
for _ in range(int(input())):
    order = list(map(str, input().split()))

    if order[0] == 'P':
        N.append(order[1])

    if order[0] == 'L':
        if N:
            N_tmp.append(N.pop())

    if order[0] == 'D':
        if N_tmp:
            N.append(N_tmp.pop())

    if order[0] == 'B':
        if N:
            N.pop()

N_tmp = reversed(N_tmp)
print("".join(N), end="")
print("".join(N_tmp))
