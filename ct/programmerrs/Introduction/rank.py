def solution(score):
    answer = [0] * len(score)
    score = sorted([[idx, i+j] for idx, [i, j] in enumerate(score)], key=lambda x:x[1], reverse=True)
    
    rank = 1
    last_score = score[0][1]
    score[0][1] = rank
    temp = 0
    
    for i in range(1, len(score)):
        if last_score == score[i][1]:
            score[i][1] = rank
            temp += 1
        else:
            rank = rank + temp + 1
            last_score = score[i][1]
            score[i][1] = rank
            temp = 0
    
    for i, j in score:
        answer[i] = j
        
    return answer


def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]