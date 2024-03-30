def solution(priorities, location):
    # 프로세스와 원래 위치를 함께 관리하기 위해 (우선순위, 원래 인덱스)의 형태로 큐를 생성
    queue = [(priority, idx) for idx, priority in enumerate(priorities)]
    print(queue)
    execution_order = 0  # 실행 순서를 계산

    while queue:
        current = queue.pop(0)  # 큐의 첫 번째 프로세스를 꺼냄
        print(current)
        # 꺼낸 프로세스보다 우선순위가 높은 프로세스가 큐에 있는지 확인
        if any(current[0] < other[0] for other in queue):
            queue.append(current)  # 더 높은 우선순위가 있다면 현재 프로세스를 큐의 끝에 다시 넣음
        else:
            # 현재 프로세스 실행 (더 높은 우선순위의 프로세스가 없을 경우)
            execution_order += 1  # 실행 순서를 1 증가
            if current[1] == location:
                # 현재 실행하는 프로세스가 찾고 있는 프로세스의 원래 위치인 경우
                return execution_order  # 현재까지의 실행 순서를 반환

def solution(priorities, location):
    answer = 0
    queue = [(prioritie, idx) for idx, prioritie in enumerate(priorities)]

    while queue:
        current = queue.pop(0)
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer



# 예제
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))  # 1
