'''
금일 코테 인증 23.06.15

관련 문제 <백준 5073> (완료)

문제 요약
삼각형의 변의 길이를 입력받고 다음과 같은 정의를 따라서 출력한다
    - Equilateral: 세 변의 길이가 모두 같은 경우
    - Isosceles: 두 변의 길이만 같은 경우
    - Scalene: 세 변의 길퍄 trc이가 모두 다른 경우
    - Invalid: 삼각형의 조건 불충분

해결 방법 및 추가 정보
삼각형의 세 변의 길이 조건
    - 가장 긴 변 < 나머지 두 변의 합
삼각형 변 조건 찾는다고 피타고라스까지 꺼냈다.. 바보 아닌가 그냥
if 순서 중요
'''
while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    max_num = max(a, b, c)
    sum_num = a + b + c
    if max_num >= sum_num - max_num:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    elif a != b != c:
        print('Scalene')

