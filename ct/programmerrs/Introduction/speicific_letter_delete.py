def solution(my_string, letter):
    answer = ''
    for s in my_string:
        if s == letter:
            pass
        else:
            answer += s
    return answer

print(solution("abcdef", "f"))