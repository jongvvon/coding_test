"""
2050. 알파벳을 숫자로 변환 D1

알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.


[제약 사항]

문자열의 최대 길이는 200이다.


[입력]

알파벳으로 이루어진 문자열이 주어진다.


[출력]

각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
"""

alphabet = list(map(str, input()))

for i in range(0, len(alphabet)):
    print(ord(alphabet[i])-64, end=" ")




# ASCII translate
# ord is chr to num
# chr is num to chr