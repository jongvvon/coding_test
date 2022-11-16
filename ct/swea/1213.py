"""
1213. [S/W 문제해결 기본] 3일차 - String D3

주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

문장의 길이는 1000자를 넘어가지 않는다.

한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.

한 문장에서는 하나의 문자열만 검색한다.

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
"""

T = 10

for case in range(1, T+1):
    num = int(input())
    word = list(input())
    sentence = list(input())

    ans = 0
    for i in range(0, len(sentence)-len(word)+1):
        count = 0
        for j in range(0, len(word)):
            if sentence[i+j] == word[j]:
                count += 1
            if count == len(word):
                ans += 1
    print("#{} {}".format(case, ans))
