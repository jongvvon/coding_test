num = int(input())
# 1 <= N <= 1,000,000
for i in range(num):
    m = 0
    n1 = i % 10
    n2 = (i % 100) // 10
    n3 = (i % 1000) // 100
    n4 = (i % 10000) // 1000
    n5 = (i % 100000) // 10000
    n6 = (i % 1000000) // 100000
    if num - (n1 + n2 + n3 + n4 + n5 + n6) == i:
        m = i
        break
print(m)
