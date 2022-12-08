import sys
input = sys.stdin.readline

queue = []
for case in range(int(input())):
    o = list(map(str, input().split()))
    order = o[0]

    if order == 'push':
        num = int(o[1])
        queue.append(num)

    elif order == 'pop':
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
