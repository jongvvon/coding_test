def solution(k, dungeons):
    visited = [False] * len(dungeons)  # 각 던전의 방문 여부를 확인하는 배열
    answer = [0]  # 탐험할 수 있는 최대 던전 수를 저장하는 배열 (변수 대신 배열 사용으로 인해 내부 함수에서 수정 가능)

    def dfs(k, count):
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:  # 아직 방문하지 않았고, 현재 피로도가 최소 필요 피로도 이상인 경우
                visited[i] = True  # 던전을 방문했다고 표시
                dfs(k - dungeons[i][1], count + 1)  # 현재 던전을 탐험한 후의 피로도와 탐험 던전 수를 가지고 다시 탐색
                visited[i] = False  # 다른 모든 경우의 수를 탐색하기 위해 방문 여부를 원래대로 되돌림

        answer[0] = max(answer[0], count)  # 현재까지 탐험한 던전 수가 이전에 탐험한 최대 던전 수보다 많다면 갱신

    dfs(k, 0)  # 초기 피로도 k와 탐험한 던전 수 0을 가지고 시작
    return answer[0]  # 탐험할 수 있는 최대 던전 수 반환

solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])


print(solution(80, [[80,20],[50,40],[30,10]]))


'''
변수 설명
k: 유저의 현재 피로도입니다.
dungeons: 각 던전별로 [최소 필요 피로도, 소모 피로도]를 나타내는 2차원 배열입니다.
visited: 각 던전의 방문 여부를 나타내는 배열입니다. 던전을 탐험했다면 True, 그렇지 않다면 False입니다.
answer: 탐험할 수 있는 최대 던전 수를 저장하는 배열입니다. 배열을 사용하는 이유는 파이썬에서는 기본 타입(int, float 등)은 immutable하기 때문에, 
내부 함수에서 이 값을 변경하고자 할 때 직접 변경이 불가능합니다. 그래서 배열과 같은 mutable한 객체를 사용하여 값을 변경합니다.

함수 설명
dfs(k, count)는 현재 피로도 k와 현재까지 탐험한 던전 수 count를 매개변수로 받습니다. 함수 내에서는 다음과 같은 작업을 수행합니다:
모든 던전에 대해서 반복문을 실행합니다. 이 때, 아직 방문하지 않았고(visited[i] == False), 
현재 피로도가 해당 던전을 탐험하기 위한 최소 필요 피로도 이상인 경우에만 다음 단계로 진행합니다.
해당 던전을 방문했다고 표시합니다(visited[i] = True).
현재 던전을 탐험한 후의 피로도(k - dungeons[i][1])와 탐험 던전 수(count + 1)를 가지고 dfs 함수를 재귀적으로 호출합니다. 
이는 다음 던전 탐험 가능성을 탐색하는 과정입니다.
재귀 호출이 끝나면, 현재 던전의 방문 여부를 다시 False로 설정하여 다른 탐색 경로에서 이 던전을 방문할 수 있도록 합니다.
모든 던전 탐색이 끝나면, 현재까지 탐험한 던전 수 count와 이전까지의 최대 탐험 던전 수 answer[0] 중 더 큰 값을 answer[0]에 저장합니다.
dfs 함수는 모든 가능한 던전 탐색 조합을 시도하며, 각 조합마다 탐험할 수 있는 최대 던전 수를 answer[0]에 업데이트합니다. 
최종적으로 answer[0]에 저장된 값이 유저가 탐험할 수 있는 최대 던전 수가 됩니다.
이 알고리즘은 모든 가능한 경우의 수를 탐색하기 때문에, 주어진 문제의 제한사항(던전의 개수가 최대 8개) 하에서는 시간 내에 충분히 해결할 수 있습니다.
'''