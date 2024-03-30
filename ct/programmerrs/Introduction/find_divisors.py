def solution(n):
    answer = set() # 완전제곱수 중복 제거를 위한 set 사용
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n//i)
    return sorted(answer)



print(solution(24))