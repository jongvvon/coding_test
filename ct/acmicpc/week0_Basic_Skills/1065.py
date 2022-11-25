num = int(input())
count = 0

for i in range(1, num+1):
    if i < 10:
        count += 1
    elif 10 <= i < 100:
        count += 1
    else:
        check = str(i)
        if int(check[1]) - int(check[0]) == int(check[2]) - int(check[1]):
            count += 1

print(count)
