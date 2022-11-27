A, B = map(int, input().split())

#최대공약수
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

#최소공배수
def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

print(GCD(A, B))
print(LCM(A, B))

'''
temp_min = []
temp_max = []
for i in range(min(A, B), 1, -1):
    if A % i == 0 and B % i == 0:
        temp_min.append(i)
for j in range(max(A, B), A*B, 1):
    if j % A == 0 and j % B == 0:
        temp_max.append(j)

print(max(temp_min))
print(min(temp_max))
'''

