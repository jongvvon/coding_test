ori = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))

for i in range(len(piece)):
    print(ori[i]-piece[i], end=" ")