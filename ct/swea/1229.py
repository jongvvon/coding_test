T = 10
for case in range(1, T+1):
    length = int(input())
    origin = list(map(int, input().split()))
    num = int(input())
    order = list(map(str, input().split()))

    for i in range(0, len(order)):
        if order[i] == 'I':
            for a in range(0, int(order[i+2])):
                origin.insert(int(order[i+1])+a, int(order[i+3+a]))
        if order[i] == 'D':
            for _ in range(0, int(order[i+2])):
                del origin[int(order[i+1])]
        else:
            continue

    print("#{}".format(case), end=" ")
    for j in range(1, 11):
        print(origin[j], end=" ")
    print()