def solution(array):
    array = sorted(array)
    print(array)
    print(len(array)//2)
    answer = array[len(array)//2]
    print(answer)
    return answer

solution([9, -1, 0])