num = int(input())
count = 0
temp = num
flag = True
while flag:
    ten = temp // 10
    one = temp % 10
    if ten == 0:
        temp = one * 10
    if ten + one >= 10:
        temp = (one * 10) + (ten + one - 10)
    else:
        temp = (one * 10) + (ten + one)
    count += 1
    if temp == num:
        flag = False

print(count)


