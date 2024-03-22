"""
한 번에 한 개의 알파벳만 변경 가능
words 내부에 존재하는 단어로만 변환 가능

ex)
begin : hit
target : cog
words : ["hot","dot","dog","lot","log","cog"]
hit -> hot -> dot -> dog -> cog (최소 4단계)

start 단어가 words 내부에 접근할 수 있는 방법
"""

from collections import deque

# 두 단어 사이에 한 글자만 다른지 확인하는 함수
def compare_words(from_word, to_word):
    diff_count = 0
    for a, b in zip(from_word, to_word):
        print (a, '', b)
        if a != b:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def solution(begin, target, words):
    # target이 words 안에 없으면 변환 불가
    if target not in words:
        return 0
    
    # 탐색을 위한 큐
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    
    while queue:
        current_word, step = queue.popleft()
        
        # 현재 단어가 target과 같으면 변환 과정의 수를 반환
        if current_word == target:
            return step
        
        # 현재 단어에서 한 글자만 바꿔서 words에 있는 단어로 변환할 수 있는 경우 큐에 추가
        for word in words:
            if compare_words(current_word, word):
                queue.append((word, step + 1))
                words.remove(word)  # 이미 방문한 단어는 제거하여 중복 방문 방지
    
    # 변환할 수 없는 경우
    return 0


begin = "hit"
target = "cog"
words = ["hot","dot","dog","lot","log","cog"]

solution(begin, target, words)