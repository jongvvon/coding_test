# def solution(arr):
#     answer = 0
#     for i in arr:
#         answer += i
#     answer = answer / len(arr)
#     return answer

# arr = [1, 2, 3, 4]

# print(solution(arr))


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(answer)
    answer = set(answer)
    answer = list(answer)
    return answer

numbers = [2, 1, 3, 4, 1]

print(solution(numbers))