def solution(A,B):
    answer = 0
    for x, y in zip(sorted(A), sorted(B, reverse=True)):
        answer += (x * y)
    return answer

A = [1, 4, 2]
B = [5, 4, 4]
solution(A, B)