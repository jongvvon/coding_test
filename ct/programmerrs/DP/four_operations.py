def solution(arr):
    # 숫자만 추출
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    # 연산자만 추출 / 시작 인덱스를 1로, 간격을 2로 설정
    ops = arr[1::2]
    
    # 메모이제이션을 위한 딕셔너리 초기화
    memo = {}
    
    # 재귀 함수 정의
    def calculate(start, end):
        # 이미 계산된 경우
        if (start, end) in memo:
            return memo[(start, end)]
        
        # 기저 사례: 숫자 하나만 있는 경우
        if start == end:
            return [nums[start]]
        
        results = []
        # 가능한 모든 분할에 대해 연산 수행
        for i in range(start, end):
            # 왼쪽과 오른쪽 부분으로 분할
            left = calculate(start, i)
            right = calculate(i + 1, end)
            # 현재 연산자
            op = ops[i]
            
            # 분할된 부분의 결과물들에 대해 연산
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)

        # 결과 메모이제이션
        memo[(start, end)] = results
        return results
    
    # 모든 연산 순서의 결과 중 최댓값 반환
    return max(calculate(0, len(nums)-1))

# 예시
arr = ["1", "-", "3", "+", "5", "-", "8"]
print(solution(arr))  # 출력: 1
