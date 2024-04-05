def solution(score):
    answer = []
    for idx, score in enumerate(score):
        answer.append([idx, sum(score)])
    answer = sorted(answer, key=lambda x:x[1])

    count = 1
    temp = 0
    for idx, score in answer:
        if temp == score:
            score = count
        else:
            score = count
        temp = score
    
    print(answer)
    return answer


solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])