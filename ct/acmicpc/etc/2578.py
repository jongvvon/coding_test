"""
2578. 빙고

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
"""

board = [list(map(int, input().split())) for _ in range(5)]
orders = sum([list(map(int, input().split())) for _ in range(5)], [])

count = 0
temp = [0] * 4

for order in orders:
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == order:
                board[i][j] == 0
                count += 1

            if count >= 15:
                for n in range(0, 5):
                    for m in range(0, 5):
                        temp[0] += board[n][m]
                        if temp[0] == 0:
                            count += 1
                        temp[1] += board[m][n]
                        if temp[1] == 0:
                            count += 1
                        if n == m:
                            temp[2] += board[n][m]
                            if temp[2] == 0:
                                count += 1
                        if n+m == 4:
                            temp[3] += board[n][m]
                            if temp[3] == 0:
                                count += 1
            if count == 3:
                print(order)
                break

