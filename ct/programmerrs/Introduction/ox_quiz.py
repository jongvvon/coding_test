def solution(quiz):
    answer = []
    for equation in quiz:
        comp = equation.replace("=", "==")
        if eval(comp):
            answer.append("O")
        else:
            answer.append("X")
    return answer


solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])