def dfs(graph, node, visited):
    count = 1 # 현재 노드를 포함하여 카운트 시작
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    return count

def solution(n, wires):
    # 인접 리스트로 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(graph)
    answer = n # 최대 송전탑 개수 차이
    for v1, v2 in wires:
        # 전선을 끊음
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = [False] * (n + 1)
        # 끊어진 한 쪽 서브그래프의 송전탑 개수를 구함
        count = dfs(graph, v1, visited)
        
        # 두 전력망의 차이를 계산
        diff = abs(count - (n - count))
        answer = min(answer, diff)
        
        # 전선을 다시 연결
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, child_node):
#         self.children.append(child_node)

#     def remove_child(self, child_node):
#         self.children = [child for child in self.children if child is not child_node]

#     def __repr__(self, level=0):
#         ret = "  " * level + repr(self.data) + "\n"
#         for child in self.children:
#             ret += child.__repr__(level + 1)
#         return ret


# # 트리 구조 생성
# root = TreeNode("Fruits")
# apple = TreeNode("Apple")
# banana = TreeNode("Banana")
# cherry = TreeNode("Cherry")

# root.add_child(apple)
# root.add_child(banana)
# root.add_child(cherry)

# # 트리 출력
# print(root)
