def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    gcd = GCD(numer, denom)

    answer.append(numer // gcd)
    answer.append(denom // gcd)

    return answer

print(solution(9, 2, 1, 3))