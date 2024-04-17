from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 맵의 크기
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동 가능한 방향: 아래, 위, 오른쪽, 왼쪽

    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # 시작점과 시작점에서의 거리

    while queue:
        x, y, dist = queue.popleft()  # 현재 위치와 현재 위치까지의 거리

        # 도착 지점에 도달했다면 거리 반환
        if x == n-1 and y == m-1:
            return dist

        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵 범위 내이고, 길인 경우 (1이면 길)
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문 처리 (다시 방문하지 않도록 0으로 변경)
                queue.append((nx, ny, dist + 1))  # 다음 위치와 거리를 큐에 추가

    # 도착 지점에 도달할 수 없는 경우
    return -1
