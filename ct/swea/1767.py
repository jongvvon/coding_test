"""
1767. [SW Test 샘플문제] 프로세서 연결하기

삼성에서 개발한 최신 모바일 프로세서 멕시노스는 가로 N개 x 세로 N개의 cell로 구성되어 있다.

1개의 cell에는 1개의 Core 혹은 1개의 전선이 올 수 있다.

멕시노스의 가장 자리에는 전원이 흐르고 있다.

Core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며,

전선은 절대로 교차해서는 안 된다.

초기 상태로는 아래와 같이 전선을 연결하기 전 상태의 멕시노스 정보가 주어진다.

(멕시노스의 가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주한다.)

▶ 최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.

   단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

위 예제의 정답은 12가 된다.

[제약 사항]

1. 7 ≤  N ≤ 12

2. Core의 개수는 최소 1개 이상 12개 이하이다.

3. 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.

[입력]

입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어지며 그 다음 줄부터 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 줄에는 N값이 주어지며, 다음 N줄에 걸쳐서 멕시노스의 초기 상태가 N x N 배열로 주어진다.

0은 빈 cell을 의미하며, 1은 core를 의미하고, 그 외의 숫자는 주어지지 않는다.

[출력]

각 테스트 케이스마다 '#X'를 찍고, 한 칸 띄고, 정답을 출력한다.

(X는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def search(x, y):
    count = 0
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if board[nx][ny] == 1:
            continue
        if 0 <= nx < num and 0 <= ny < num:
            search(nx, ny)
        else:
            continue
    return count


for case in range(1, int(input())+1):
    num = int(input())
    board = [list(map(int, input().split())) for _ in range(num)]

    for i in range(0, num):
        for j in range(0, num):
            if board[i][j] == 1:
                search(i, j)
