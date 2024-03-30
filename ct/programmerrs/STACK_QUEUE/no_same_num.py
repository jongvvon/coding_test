def solution(arr):
    answer = []
    for num in arr:
        try:
            if answer[-1] == num:
                pass
            else:
                answer.append(num)
        except:
            answer.append(num)
            
    return answer
 

def solution(arr):
    answer = []
    answer.append(arr.pop(0))
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
        else:
            pass
    return answer

print(solution([1,1,3,3,0,1,1]))