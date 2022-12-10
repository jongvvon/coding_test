import collections

N = int(input())
deque = [i for i in range(1, N+1)]
deque = collections.deque(deque)

while len(deque) != 1:
    deque.popleft()
    deque.append(deque.popleft())

print(*deque)
