def solution(my_string):
    temp = ''
    array = []
    for str in my_string:
        if str.isdigit():
            temp += str
        else:
            if temp != '':
                array.append(int(temp))
            temp = ''
    # 숫자로 str 탐색이 끝난 경우
    if temp != '':
        array.append(int(temp))
    return sum(array)


print(solution("a1b23"))