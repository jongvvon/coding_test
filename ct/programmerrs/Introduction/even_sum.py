def solution(n):
    return sum([num for num in range(n+1) if num % 2 == 0])

print(solution(10))