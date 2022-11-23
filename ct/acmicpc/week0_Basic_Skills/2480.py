n1, n2, n3 = map(int, input().split())

if n1 == n2 == n3:
    print(n1 * 1000 + 10000)
elif n1 == n2:
    print(n1 * 100 + 1000)
elif n2 == n3:
    print(n2 * 100 + 1000)
elif n3 == n1:
    print(n3 * 100 + 1000)
else:
    print(max(n1, n2, n3) * 100)
