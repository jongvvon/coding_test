import sys
input = sys.stdin.readline

N = int(input())

serial = []
for _ in range(N):
    num = input().rstrip()
    temp = 0
    for i in num:
        if 48 <= ord(i) <= 57:
            temp += int(i)
    serial.append([num, temp])

dict_sort_serial = sorted(serial, key=lambda x: x[0])
num_sort_serial = sorted(dict_sort_serial, key=lambda x: x[1])
len_sort_serial = sorted(num_sort_serial, key=lambda x: len(x[0]))

for num, temp in len_sort_serial:
    print(num)
