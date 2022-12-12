def hanoi(idx, start, end, sub):
    if idx == 1:
        print(start, end)
        return
    else:
        hanoi(idx-1, start, sub, end)
        print(start, end)
        hanoi(idx-1, sub, end, start)


num = int(input())
print(2**num-1)
hanoi(num, "1", "3", "2")