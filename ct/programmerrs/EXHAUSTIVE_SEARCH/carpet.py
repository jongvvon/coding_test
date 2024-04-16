def solution(brown, yellow):
    answer = []
    cells = brown + yellow
    temp = []
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            temp.append([i, yellow//i])
    
    for w, h in temp:
        if cells == (w+2) * (h+2):
            return [h+2, w+2]

    
    print(temp)
    return answer


print(solution(10, 2))
print(solution(24, 24))