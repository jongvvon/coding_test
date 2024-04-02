def prime_num(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(i)

prime_num(100)