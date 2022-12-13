array = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]
temp = 0
while array != answer:
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            print(*array)