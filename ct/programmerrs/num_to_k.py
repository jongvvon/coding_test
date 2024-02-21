def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

    
def main():
    print(solution([1, 5, 2, 6, 3, 7, 4],
             [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

if __name__ == "__main__":
    main()