# def solution(s):
#     answer = ''
#     for i in range(len(s)):
#         try:
#             if int(s[i]):
#                 answer += i
#         except:
#             if s[i-1] == ' ':
#                 answer += s[i].upper()
#             else:
#                 answer += s[i].lower()
#     return answer

def solution(s):
    answer = ''
    words = [word.lower() for word in s.split(' ')]
    for i in words:
        if i:  # 단어가 비어있지 않은 경우만 처리
            answer += i[0].upper() + i[1:] + ' '
        else:  # 단어가 비어있는 경우(연속된 공백 등), 공백만 추가
            answer += ' '
    return answer[:-1]


print(solution("3people unFollowed me"))