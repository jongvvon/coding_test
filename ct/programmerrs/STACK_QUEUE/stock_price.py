def solution(prices):
    answer = []
    flag = True
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                flag = False
                break
        if flag:
            answer.append(len(prices) - i - 1)
        flag = True

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))