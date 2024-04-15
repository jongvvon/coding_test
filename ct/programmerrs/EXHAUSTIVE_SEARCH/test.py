def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * ((len(answers) // 5) + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * ((len(answers) // 8) + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((len(answers) // 10) + 1)
    score = [0, 0, 0]

    for a, f, s, t in zip(answers, first[:len(answers)], second[:len(answers)], third[:len(answers)]):
        # print(a, f, s, t)
        if a == f:
            score[0] += 1
        if a == s:
            score[1] += 1
        if a == t:
            score[2] += 1

    max_score = max(score)
    answer = [idx + 1 for idx, value in enumerate(score) if value == max_score]

    return answer

print(solution([1,2,3,4,5]))
