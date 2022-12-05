import sys
input = sys.stdin.readline

T = int(input())
for case in range(T):
    ps = input()
    array = []
    for i in ps:
        if i == '(':
            array.append(0)
        elif i == ')':
            if 0 in array:
                array.remove(0)
            else:
                array.append(1)

    if 1 in array or array:
        print("NO")
    else:
        print("YES")
