from collections import Counter

def solution(array):
    array_counter = Counter(array)
    answer = [k for k, v in array_counter.items() if v == max(array_counter.values())]
    if len(answer) != 1:
        answer = -1
    else:
        answer = answer[0]
    return answer

print(solution([1]))



def solution(array):
    while len(array) != 0:
        # enumerate는 각 원소와 그 원소의 인덱스를 제공
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
