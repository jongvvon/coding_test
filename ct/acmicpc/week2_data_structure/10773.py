import sys
input = sys.stdin.readline

array = []
for case in range(int(input())):
    num = int(input())
    if array and num == 0:
        array.pop()
    else:
        array.append(num)

print(sum(array))