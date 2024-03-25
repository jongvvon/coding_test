def solution(dots):
    # 기울기를 계산하는 함수
    def slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    # 가능한 모든 직선 쌍의 기울기를 저장할 리스트
    slopes = []
    
    # 네 점을 이은 모든 직선의 기울기를 계산하여 slopes에 저장
    for i in range(4):
        for j in range(i+1, 4):
            slopes.append(slope(dots[i], dots[j]))
    
    # slopes에 저장된 기울기들을 비교하여 평행한 직선 쌍이 있는지 확인
    for i in range(len(slopes)):
        for j in range(i+1, len(slopes)):
            if slopes[i] == slopes[j]:
                return 1
    
    # 평행한 직선 쌍이 없으면 0 반환
    return 0


def calculate_slope(x1, y1, x2, y2):
    # 분모가 0이 되는 경우를 방지하기 위해 기울기를 계산할 때 분모에 작은 값을 더함
    return (y2 - y1) / (x2 - x1)

def solution(dots):
    # 각 조합에 대한 기울기 계산
    slopes = []
    slopes.append(calculate_slope(dots[0][0], dots[0][1], dots[1][0], dots[1][1]))
    slopes.append(calculate_slope(dots[2][0], dots[2][1], dots[3][0], dots[3][1]))
    slopes.append(calculate_slope(dots[0][0], dots[0][1], dots[2][0], dots[2][1]))
    slopes.append(calculate_slope(dots[1][0], dots[1][1], dots[3][0], dots[3][1]))
    slopes.append(calculate_slope(dots[0][0], dots[0][1], dots[3][0], dots[3][1]))
    slopes.append(calculate_slope(dots[1][0], dots[1][1], dots[2][0], dots[2][1]))
    
    # slopes 리스트는 총 6개의 기울기 값을 포함하고 있으며, 이 중 어느 두 값이든 같다면 평행한 직선이 존재함을 의미
    # 기울기를 비교하여 평행한 경우가 있는지 확인
    for i in range(6):
        for j in range(i+1, 6):
            # i번째 기울기와 j번째 기울기가 같은 경우 평행한 직선이 존재
            if slopes[i] == slopes[j]:
                return 1
                
    return 0  # 평행한 직선이 없음


def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solution(dots):
    # 1,2번 좌표와 3,4번 좌표로 만들어진 직선의 기울기 계산
    slope1 = calculate_slope(dots[0][0], dots[0][1], dots[1][0], dots[1][1])
    slope2 = calculate_slope(dots[2][0], dots[2][1], dots[3][0], dots[3][1])
    
    # 두 기울기가 같은지 비교하여 평행 여부 확인
    if slope1 == slope2:
        return 1  # 평행
    else:
        return 0  # 평행하지 않음

def solution(dots):
    # 각 쌍에 대한 기울기 계산
    slope_pairs = [
        (calculate_slope(dots[0][0], dots[0][1], dots[1][0], dots[1][1]), calculate_slope(dots[2][0], dots[2][1], dots[3][0], dots[3][1])),
        (calculate_slope(dots[0][0], dots[0][1], dots[2][0], dots[2][1]), calculate_slope(dots[1][0], dots[1][1], dots[3][0], dots[3][1])),
        (calculate_slope(dots[0][0], dots[0][1], dots[3][0], dots[3][1]), calculate_slope(dots[1][0], dots[1][1], dots[2][0], dots[2][1]))
    ]
    
    # 각 쌍의 기울기를 비교하여 평행 여부 확인
    for slope1, slope2 in slope_pairs:
        if slope1 == slope2:
            return 1  # 평행한 경우 발견
    return 0  # 모든 쌍에 대해 평행하지 않음


def solution(dots):
    # 비구조화 할당, 구조분해
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0


print(solution([[1, 4], [3, 8], [5, 12], [11, 6]]))