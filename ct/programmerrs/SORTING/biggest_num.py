def solution(numbers):
    answer = ''
    # 모든 경우의 수를 만들어 최대값 찾기 (조합?) -> 형변환을 많이해야 될 것으로 예상됨
    # 최대의 수가 되도록 비교하여 찾기 -> 공식 -> complicate
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return answer if answer[0] != '0' else '0'


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))