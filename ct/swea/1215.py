"""
1215. [S/W 문제해결 기본] 3일차 - 회문1 D3

"기러기", "토마토", "스위스"와 같이 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.

위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개이므로 4를 반환하면 된다.

[제약 사항]

각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.

ABA도 회문이며, ABBA도 회문이다. A 또한 길이 1짜리 회문이다.

가로 또는 세로로 이어진 회문의 개수만 센다.

아래 그림에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

[입력]

총 10개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.
"""
T = 10

for case in range(1, T+1):
    length = int(input())
    board = [list(input()) for _ in range(8)]

    # for i in board:
    #     print(*i)

    ans = 0
    for i in range(0, 8):
        for j in range(0, 8):
            low_temp = []
            col_temp = []
            for k in range(0, length):                              # 문제에서 제시한 길이만큼 접근
                if j < 8 - length + 1:                              # 전체 배열 사이즈 - 제시한 길이
                    low_temp.append(board[i][j + k])
                if i < 8 - length + 1:
                    col_temp.append(board[i + k][j])
            if "".join(low_temp) == "".join(reversed(low_temp)):    # 앞뒤로 같은지 확인
                if low_temp:                                        # 빈 리스트일 경우 예외 처리
                    ans += 1
            if "".join(col_temp) == "".join(reversed(col_temp)):
                if col_temp:
                    ans += 1
            # print(low_temp, col_temp, ans)

    print("#{} {}".format(case, ans))
