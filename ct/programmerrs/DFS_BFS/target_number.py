def solution(numbers, target):
    answer = 0

    # 재귀 함수 정의
    def dfs(index, current_sum):
        print(current_sum)
        nonlocal answer  # 바깥쪽 스코프의 answer 변수 사용
        # 종료 조건: 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 현재 합이 타겟 넘버와 같다면, 방법의 수를 1 증가
            if current_sum == target:
                answer += 1
            return
        
        # 현재 숫자를 더하는 경우
        dfs(index + 1, current_sum + numbers[index])
        # 현재 숫자를 빼는 경우
        dfs(index + 1, current_sum - numbers[index])
    
    # 재귀 함수 시작
    dfs(0, 0)
    
    return answer


print(solution([1,1,1,1,1], 3))