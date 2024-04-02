def solution(my_string):
    answer = 0
    flag = True
    for s in my_string.split():
        if s.isdigit():
            if flag:
                answer += int(s)
            else:
                answer -= int(s)
        else:
            if s == '+':
                flag = True
            else:
                flag = False

    return answer


solution("3 + 4 - 1 + 2")