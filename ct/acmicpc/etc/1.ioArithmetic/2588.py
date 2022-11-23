num_x = int(input())
num_y = map(int, input())
num_y = list(num_y)

a = num_x * num_y[2]
print(a)
b = num_x * num_y[1]
print(b)
b = b * 10
c = num_x * num_y[0]
print(c)
c = c * 100
print(a + b + c)