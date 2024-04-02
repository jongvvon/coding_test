solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

"""
주어진 람다 함수 solution은 두 개의 매개변수 a와 n을 받습니다. 
여기서 a는 숫자들의 리스트이고, n은 특정 숫자입니다. 
이 함수는 리스트 a 내의 요소들을, 각 요소와 n의 절대 차이값을 기준으로 정렬하고, 그 중 절대 차이가 가장 작은 요소를 반환합니다. 
만약 절대 차이값이 같은 요소가 여러 개 있을 경우, 그 중 숫자 자체가 작은 요소를 반환합니다.

함수 설명
sorted(a, key=lambda x: (abs(x-n), x)): 이 부분은 리스트 a를 정렬하는데, 정렬 기준은 두 가지입니다. 
첫 번째 기준은 x와 n의 절대 차이 abs(x-n)이고, 두 번째 기준은 x 값 자체입니다. 
이렇게 두 기준을 튜플로 묶어 key 인자로 제공하면, 파이썬은 먼저 첫 번째 기준으로 정렬을 시도하고, 그 값이 같으면 두 번째 기준으로 정렬합니다.
[0]: 정렬된 리스트의 첫 번째 요소를 반환합니다. 이는 절대 차이가 가장 작은 요소 중에서도 가장 작은 숫자를 의미합니다.
"""

def solution(array, n):
    array = sorted(array)
    abs_num = [abs(num-n) for num in array]
    return array[abs_num.index(min(abs_num))]