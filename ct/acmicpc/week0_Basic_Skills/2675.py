for case in range(0, int(input())):
    num, word = map(str, input().split())
    for i in word:
        for _ in range(int(num)):
            print(i, end="")
    print()