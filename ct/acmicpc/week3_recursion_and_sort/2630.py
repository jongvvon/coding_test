N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0


def check_square(idx, square):
    global white
    global blue
    n_curr = len(square)
    if idx == 0:
        return
    sum_square = sum([sum(square[i]) for i in range(n_curr)])
    if sum_square == 0:
        white += 1
        return
    if sum_square == n_curr * n_curr:
        blue += 1
        return
    else:
        temp_square = [square[i][0:n_curr//2] for i in range(0, n_curr//2)]
        check_square(idx//2, temp_square)
        temp_square = [square[i][n_curr//2:n_curr] for i in range(0, n_curr//2)]
        check_square(idx//2, temp_square)
        temp_square = [square[i][n_curr//2:n_curr] for i in range(n_curr//2, n_curr)]
        check_square(idx//2, temp_square)
        temp_square = [square[i][0:n_curr//2] for i in range(n_curr//2, n_curr)]
        check_square(idx//2, temp_square)


check_square(N, array)
print(white)
print(blue)
