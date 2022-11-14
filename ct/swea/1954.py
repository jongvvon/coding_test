"""
1954. 달팽이 숫자 D2

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N 크기의 달팽이를 출력하시오.

[예제]

N이 3일 경우,
    1   2   3
    8   9   4
    7   6   5

N이 4일 경우,
    1   2   3   4
    12  13  14  5
    11  16  15  6
    10  9   8   7

[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.

[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""


direction_x = [0, 1, 0, -1]
direction_y = [1, 0, -1, 0]

for case in range(1, int(input())+1):
    num = int(input())
    snail = [[0] * num for _ in range(num)]

    x, y = 0, 0
    dist = 0

    for n in range(1, num*num+1):
        snail[x][y] = n
        x += direction_x[dist]
        y += direction_y[dist]

        if x < 0 or y < 0 or x >= num or y >= num or snail[x][y] != 0:
            x -= direction_x[dist]
            y -= direction_y[dist]

            dist = (dist + 1) % 4

            x += direction_x[dist]
            y += direction_y[dist]

    print("#{}".format(case))
    for i in snail:
        print(*i)
