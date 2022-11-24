for case in range(0, int(input())):
    data = list(map(int, input().split()))
    temp = sum(data[1:]) / data[0]
    ans = 0
    for i in range(1, len(data)):
        if data[i] > temp:
            ans += 1
    print("{:.3f}%".format(ans / data[0] * 100))
