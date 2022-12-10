import collections
import sys
input = sys.stdin.readline

T = int(input())
for case in range(T):
    p = input().rstrip()
    n = int(input())
    array = input().rstrip()
    array = array[1:-1].split(",")
    array = collections.deque(array)
    if n == 0:
        print("error")
        break
    for i in p:
        if i == "R":
            array.reverse()
        if i == "D":
            if array:
                array.popleft()
            else:
                print("error")
                break

    print('[' + ','.join(map(str, array)) + ']')
