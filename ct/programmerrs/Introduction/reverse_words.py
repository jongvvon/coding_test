# def solution(my_string):
#     answer = ''
#     for i in range(len(my_string)-1, -1, -1):
#         answer += my_string[i]
#     return answer


def solution(my_string):
    return my_string[::-1]

print(solution("jaron"))