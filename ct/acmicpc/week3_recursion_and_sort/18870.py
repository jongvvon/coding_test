N = int(input())
coordinate = list(map(int, input().split()))

# sort_coordinate = list(set(sorted(coordinate)))
sort_coordinate = sorted(list(set(coordinate)))

compression_coordinate = {sort_coordinate[i]: i for i in range(len(sort_coordinate))}

for i in coordinate:
    print(compression_coordinate[i], end=" ")
