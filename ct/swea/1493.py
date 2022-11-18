"""
1493. 수의 새로운 연산 D3

2차원 평면 제 1사분면 위의 격자점 (x,y)에 위 그림과 같이 대각선 순서로 점에 수를 붙인다.

점 (x,y)에 할당된 수는 #(x,y)로 나타낸다.

예를 들어 #(1,1) = 1, #(2,1)=3, #(2,2) = 5, #(4,4) = 25이다.

반대로 수 p가 할당된 점을 &(p)로 나타낸다.

예를 들어 &(1) = (1,1), &(3) = (2,1), &(5) = (2,2), &(25) = (4,4)이다.

두 점에 대해서 덧셈을 정의한다. 점 (x,y)와 점 (z,w)를 더하면 점 (x+z, y+w)가 된다.

즉, (x,y) + (z,w) = (x+z, y+w)로 정의한다.

우리가 해야 할 일은 수와 수에 대한 새로운 연산 ★를 구현하는 것으로, p★q는 #(&(p)+&(q))으로 나타난다.

예를 들어, &(1)=(1,1), &(5) = (2,2)이므로, 1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13이 된다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 p,q(1 ≤ p, q ≤ 10,000)가 주어진다.

[출력]

각 테스트 케이스마다 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 각 테스트 케이스마다 p★q의 값을 출력한다.
"""

graph = [[1, 3, 6, 10], [2, 5, 9, 14], [4, 8, 13, 19], [7, 12, 18, 25]]

for case in range(1, int(input())+1):
    p, q = map(int, input().split())

    ptemp = []
    qtemp = []
    for i in range(0, len(graph)):
        if p in graph[i]:
            ptemp.append(i)
            ptemp.append(graph[i].index(p))
        if q in graph[i]:
            qtemp.append(i)
            qtemp.append(graph[i].index(q))

    ans = []
    for j in range(0, len(ptemp)):
        ans.append(ptemp[j]+qtemp[j]+1)

    print("#{} {}".format(case, graph[ans[0]][ans[1]]))