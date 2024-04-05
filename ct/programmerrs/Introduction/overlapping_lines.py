def solution(lines):
    events = []
    for start, end in lines:
        # 시작 지점과 끝 지점을 이벤트로 추가
        # 시작 이벤트는 선분 수 증가, 끝 이벤트는 선분 수 감소
        events.append((start, "start"))
        events.append((end, "end"))
    
    # 이벤트를 시간 순으로 정렬
    events.sort()
    
    overlap_length = 0
    current_overlap = 0
    for i in range(len(events)):
        event_time, event_type = events[i]
        
        if event_type == "start":
            current_overlap += 1
        else:
            current_overlap -= 1
        
        # 겹치는 선분이 2개 이상일 경우, 겹치는 길이 계산
        if current_overlap >= 2:
            # 다음 이벤트와의 시간 차이 계산
            if i + 1 < len(events):
                next_event_time, _ = events[i + 1]
                overlap_length += next_event_time - event_time
    
    return overlap_length
