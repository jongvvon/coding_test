def solution(n):
    answer = []
    temp = ''
    for i in range(1, 101):
        if i % 3 == 0:
            continue
        for j in str(i):
            if '3' in j:
                temp = ''
                break
            else:
                temp += j
        if temp != '':
            answer.append(int(temp))
            temp = ''
            
    print(answer)
    
    return answer[n-1]

def solution(n):
    answer = []
    for i in range(1, 101):
        # 3의 배수가 아니고, 숫자에 '3'이 포함되지 않는 경우
        if i % 3 != 0 and '3' not in str(i):
            answer.append(i)
    
    # n번째 요소를 반환하기 전에 answer의 길이 확인
    if len(answer) >= n:
        return answer[n-1]
    else:
        # answer에 n개의 요소가 없는 경우 오류 메시지 반환 또는 적절한 예외 처리
        return "Index out of range"  # 또는 다른 적절한 예외 처리

# 테스트
print(solution(10))  # 예를 들어, n=10일 때

def solution(n):
    count = 0  # 조건을 만족하는 숫자의 개수를 세는 변수
    num = 1    # 검사를 시작할 첫 번째 숫자
    
    while True:
        if num % 3 != 0 and '3' not in str(num):
            count += 1
            if count == n:
                return num
        num += 1