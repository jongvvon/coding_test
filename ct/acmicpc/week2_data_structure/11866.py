import sys
import collections
input = sys.stdin.readline

N, K = map(int, input().split())
array = [i for i in range(1, N+1)]
deque = collections.deque(array)
answer = []

while len(answer) != N:
    for _ in range(K-1):
        deque.append(deque.popleft())
    answer.append(deque.popleft())

print("<", end="")
for i in range(len(answer)-1):
    print("{},".format(answer[i]), end=" ")
print("{}>".format(answer[-1]))
