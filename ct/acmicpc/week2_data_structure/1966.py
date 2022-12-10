import sys
import collections
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    imp = collections.deque(imp)
    idx = collections.deque(idx)
    idx[M] = 'target'
    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.popleft()
                idx.popleft()

        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())
