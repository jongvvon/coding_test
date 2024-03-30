def solution(progresses, speeds):
    answer = []
    # 각 기능이 완료되기까지 필요한 날짜를 저장할 리스트
    days_left = []
    
    for progress, speed in zip(progresses, speeds):
        # 완료까지 남은 진척도
        remaining_progress = 100 - progress
        # 완료까지 남은 일수 계산
        if remaining_progress % speed == 0:
            days_left.append(remaining_progress // speed)
        else:
            days_left.append((remaining_progress // speed) + 1)
    print(days_left)

    # 현재 기준이 되는 완료일
    current_day = days_left[0]
    # 현재 배포될 기능의 수
    count = 1
    for i in range(1, len(days_left)):
        # 만약 현재 기능이 기준 완료일보다 더 많은 시간이 필요하다면
        if days_left[i] > current_day:
            # 지금까지의 기능을 배포하고 새로운 기준일과 카운트를 설정
            answer.append(count)
            current_day = days_left[i]
            count = 1
        else:
            # 현재 기능도 함께 배포할 수 있으므로 카운트 증가
            count += 1
    
    # 마지막 배포 추가
    answer.append(count)
    
    return answer


def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):
        if (100 - progress) % speed == 0:
            days.append((100 - progress) // speed)
        else:
            days.append((100 - progress) // speed + 1)
    target = days[0]
    count = 1
    for i in range(1, len(days)):
        if days[i] <= target:
            count += 1
        else:
            answer.append(count)
            target = days[i]
            count = 1

    answer.append(count)

    return answer





progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))