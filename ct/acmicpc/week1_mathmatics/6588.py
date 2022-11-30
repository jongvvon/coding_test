import math
import sys
input = sys.stdin.readline

sieve = []

sieve = [True] * (1000000 + 1)

for i in range(2, int(math.sqrt(1000000)) + 1):
    if sieve[i]:
        for j in range(i + i, 1000000 + 1, i):
            sieve[j] = False


while True:
    num = int(input())
    if num == 0:
        break

    for k in range(2, len(sieve)):
        if sieve[k] and sieve[num - k]:
            print("{} = {} + {}".format(num, k, num - k))
            break
