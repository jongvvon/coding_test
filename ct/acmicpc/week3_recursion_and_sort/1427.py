n = input()
array = []
for i in n:
    array.append(int(i))

sort_array = sorted(array, reverse=True)

for j in sort_array:
    print(j, end="")
print()