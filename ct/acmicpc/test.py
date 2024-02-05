def solution(numbers):
    # 정답 정보
    answer = [-1] * len(numbers)
    # 스택
    stack = []
    for idx, num in enumerate(numbers):
        # 큰 수가 나온 경우, 그 수를 사용해 정답 정보 갱신
        # while stack and numbers[stack[-1]] < num:  # 정상
        # while numbers[stack[-1]] < num and stack:   # 오류 발생
        while numbers[stack[-1]] < num:    # 정상
            if stack:
                answer[stack.pop()] = num
            else:
                break
        stack.append(idx)

    print(answer)


numbers = [2, 3, 3, 5]
solution(numbers)