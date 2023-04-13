'''
금일 코테 인증 23.04.12

관련 문제 <백준 1697> (완료)

문제 요약
이동 방식 -> 걷기(X-1, X+1) / 순간이동(2X), 1초 마다 수행, 두 점이 가장 빨리 만나는 시간

해결 방법 및 추가 정보
두 가지의 이동 방식을 이용하여 최단 시간을 구하는 것은 곳 최단 경로를 뜻하기 때문에 bfs 이용
기본적인 bfs 문제라고 생각했지만 고려해야 될 사항들이 꽤 많았다.
1. 방문 여부와 움직임을 저장할 배열을 처음엔 따로 지정해주었으나 한개의 배열에서 값을 변경하는 방법으로 메모리 누수를 줄임
2. 100000 까지가 input 이긴 하지만 이것보다 큰 수에서 -1 을 통해 내려오는 경우가 더 빠를 수도 있지 않을까? 하는 의문에서
찾아보았다. 2a-2 기준으로 a -> 2a -> 2a-1 -> 2a-2 보다 a -> a-1 -> 2a-2 가 움직임이 더 적기때문에 고려하지 않아도 됨
3. 0 보다 작아지는 경우의 예외처리와 원하는 값을 얻은 뒤 메모리 누수를 막기위한 예외처리도 필요했음.
'''
from collections import deque

k, n = map(int, input().split())
dist = [-1] * 100001
#invited = [False] * 100000

def bfs(curr):
    q = deque()
    q.append(curr)
    while q:
        point = q.popleft()
        # 걷기 혹은 순간이동 모든 방식에 대한 bfs
        for i in (point - 1, point + 1, point * 2):
            # n에 가장 빨리 도착하는 이후를 계산할 필요가 있는가?
            # 메모리 사용을 줄이기 위한 조건문
            if dist[n] != -1:
                return
            # a -> 2a -> 2a-1 -> 2a-2 / a -> a-1 -> 2a-2
            # 후자가 더 빠른(움직임이 적은) 양상을 보이기 때문에 100,000 초과는 고려하지 않아도 됨
            if i < 0 or i > 100000:
                continue
            # invited[i] == False
            # 즉, 가장 빨리 n에 도착하는 움직임이 최단 시간이다.
            if dist[i] == -1:
                # 이전까지의 움직임 + 1 을 현재 i 에 입력 
                dist[i] = dist[point] + 1
                q.append(i)
            

dist[k] = 0
bfs(k)
# print(dist[:2*n])
print(dist[n])