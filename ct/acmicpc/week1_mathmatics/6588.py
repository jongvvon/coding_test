def prime_list(n):
    sieve = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    if sieve[n]:
        return True
    else:
        return False


flag = True
while flag:
    num = int(input())
    if num == 0:
        flag = False
        break

    for i in range(2, num//2):
        for j in range(num, num//2, -1):
            if prime_list(i) and prime_list(j):
                if i + j == num:
                    print("{} = {} + {}".format(num, i, j))

