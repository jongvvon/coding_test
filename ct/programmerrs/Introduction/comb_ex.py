from itertools import combinations

def solution(balls, share):
    return len(list(combinations(range(balls), share)))

from math import factorial, comb

def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls - share))

def solution(balls, share):
    return comb(balls, share)

print(solution(3, 2))