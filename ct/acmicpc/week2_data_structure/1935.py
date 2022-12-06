import sys

T = int(input())
pbm = input()
nums = [input() for _ in range(T)]

array = []
answer = ''
for i in range(len(pbm)):
    if 65 <= ord(pbm[i]) <= 90:
        array.append(nums[ord(pbm[i])-65])
    else:
        answer += array[-2]
        answer += pbm[i]
        answer += array[-1]
        array.pop()
        array.pop()
        answer = str(eval(answer))
        array.append(answer)
        answer = ''

answer = float(array[0])
print("{0:.2f}".format(answer))
