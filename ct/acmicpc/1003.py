"""
1003. 피보나치 함수 S3
'dynamic programming'
"""

zero = [0] * 42
one = [0] * 42
zero[0], zero[1], one[0], one[1] = 1, 0, 0, 1

T = int(input())

for case in range(1, T+1):
    num = int(input())
    for j in range(num):
        zero[j+2] = zero[j+1] + zero[j]
        one[j+2] = one[j+1] + one[j]
    print("{} {}".format(zero[num], one[num]))
