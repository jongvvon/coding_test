def hanoi(idx, start, end, sub):
    if idx == 1:
        if num <= 20:
            print(start, end)
        return
    else:
        hanoi(idx-1, start, sub, end)
        if num <= 20:
            print(start, end)
        hanoi(idx-1, sub, end, start)


num = int(input())
print(2 ** num-1)
if num <= 20:
    hanoi(num, "1", "3", "2")
