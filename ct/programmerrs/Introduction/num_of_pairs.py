import math

def solution(n):
    answer = 0
    for i in range(1, round(math.sqrt(n))+1):
        if n % i == 0:
            if n // i == i:
                answer += 1
            else:
                answer += 2
    return answer


print(solution(20))