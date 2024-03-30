def solution(emergency):
    return [idx + 1 for num in emergency for idx, priority in [(idx, priority) for idx, priority in enumerate(sorted(emergency, reverse=True))] if priority == num]


emergency = [3, 76, 24]
print(solution(emergency))