"""
7510. 상원이의 연속 합 D3

연속적인 것에는 어떤 아름다움이 있다.

상원이는 자연수를 아름답게 쓰는 법을 고민하다가 연속된 자연수의 합으로 표현하기로 했다.

예를 들면, 15는 15 = 7 + 8 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5 로 4가지 방법이 있다.

아름다운 건 다다익선이라고 생각하는 상원이는 표현하고 싶은 자연수 N이 얼마나 많은 경우로 표현될 수 있는 지 궁금해졌다.

상원이를 도와서 문제를 해결하자.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 표현하고 싶은 자연수 N(1 ≤ N ≤ 106)이 주어진다.

[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

N을 연속된 자연수의 합으로 표현할 수 있는 경우의 수를 출력하라.
"""

for case in range(1, int(input())+1):
    num = int(input())
    temp = num // 2
    val = 0
    ans = 1
    flag = True
    while flag:
        for i in range(1, temp+1):
            val += i
            if val > num:
                break
            if val == num:
                ans += 1
    print(ans)