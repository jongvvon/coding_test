import sys
import collections
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
element = list(map(int, input().split()))
deque = [i for i in range(1, N + 1)]
deque = collections.deque(deque)
array = []
temp = 0
cnt = 0
while element != array:
    for i in range(M):
        # print(element, array)
        if deque[0] == element[i]:
            array.append(deque.popleft())
        else:
            deque_l = copy.deepcopy(deque)
            deque_r = copy.deepcopy(deque)
            cnt_l = 0
            cnt_r = 0
            while deque_l[0] != element[i]:
                deque_l.append(deque_l.popleft())
                cnt_l += 1
            while deque_r[0] != element[i]:
                deque_r.appendleft(deque_r.pop())
                cnt_r += 1
            # print(cnt_l, cnt_r, cnt)
            if cnt_l < cnt_r:
                array.append(deque_l.popleft())
                cnt += cnt_l
                deque = deque_l
            else:
                array.append(deque_r.popleft())
                cnt += cnt_r
                deque = deque_r

print(cnt)
