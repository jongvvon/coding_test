# Padovan Seqeunce
# P(0) = P(1) = P(2) = 1
# P(n) = P(n-2) + P(n-3)
# P(n-3) = P(n-2) - P(n)
# same the fibonacci sequence

Padovan = [0] * 100
def padovan(i):
    if i == 0 or i == 1 or i == 2:
        return 1
    if Padovan[i] != 0:
        return Padovan[i]
    Padovan[i] = padovan(i - 2) + padovan(i - 3)
    return Padovan[i]


for case in range(int(input())):
    num = int(input())
    print(padovan(num-1))

