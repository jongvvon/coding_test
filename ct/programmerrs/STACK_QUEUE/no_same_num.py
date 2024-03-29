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
 

print(solution([1,1,3,3,0,1,1]))