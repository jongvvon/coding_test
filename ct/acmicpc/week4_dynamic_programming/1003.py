# fibonacci function 
x, y = 0, 0

# defult fibonacci function -> using recursive
def fibonacci(n):
    if n == 0:
        print('0')
        return 0
    elif n == 1:
        print('1')
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# fibonacci function -> dynamic programmin / bottom-up
def fib_bottom_up(n):
    fib_table = [[0 for _ in range(2)] for _ in range(n + 1)]

    # fib_table[n][0], fib_table[n][1] => count 0 for n, count 1 for n
    fib_table[0][0], fib_table[0][1] = 1, 0
    if n == 0:
        return fib_table[n][0], fib_table[n][1]
    
    fib_table[1][0], fib_table[1][1] = 0, 1
    if n == 1:
        return fib_table[n][0], fib_table[n][1]

    for i in range(2, n + 1):
        fib_table[i][0] = fib_table[i-1][0] + fib_table[i-2][0]
        fib_table[i][1] = fib_table[i-1][1] + fib_table[i-2][1]
    
    return fib_table[n][0], fib_table[n][1]


for _ in range(int(input())):
    n = int(input())
    print(*fib_bottom_up(n))