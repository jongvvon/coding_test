def solution(n):
    for i in range(1, 11):
        n = n // i
        print(n, '', i)
        if n == 1 or i == n:
            return i

solution(64)