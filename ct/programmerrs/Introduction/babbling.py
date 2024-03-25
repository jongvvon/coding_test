default = ['aya', 'ye', 'woo', 'ma']

def solution(babbling):
    answer = 0
    word = ''
    flag = False
    for babble in babbling:
        for str in babble:
            word += str
            if word in default:
                flag = True
                word = ''
        if word != '':
            flag = False
        if flag:
            answer += 1
        word = ''
    return answer

import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt

solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])