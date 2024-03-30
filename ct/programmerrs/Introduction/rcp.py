def solution(rsp):
    r = "0"
    c = "2"
    p = "5"
    answer = ''
    for str in rsp:
        if str is r:
            answer += p
        if str is c:
            answer += r
        if str is p:
            answer += c
    return answer

def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

print(solution("205"))