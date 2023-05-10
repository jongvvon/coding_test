'''
금일 코테 인증 23.05.04

관련 문제 <백준 1991: 트리 순회> (완료)

문제 요약
트리를 입력받고 전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램을 구하시오

해결 방법 및 추가 정보
root를 기준으로 잡아 왼쪽, 오른쪽 방향만 정해주면 되는 할만한 문제였던 것 같다.
'''
import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')

'''
저는 소묘같은 사람입니다. 
잘못그려도 언제든지 수정할 수 있기에
경험의 부족으로 서툴 수 있지만 
옳은 방향으로 이끌어주는 해당 회사의 강점이라면 
저를 더욱 아름다운 그림으로 만들 수 있을 것이라고 생각합니다.

연필로 그리는 것도 중요한데 지우개를 쓰는 방법을 아는것도 중요합니다.
앞으로 계속 나아가는 방향만 생각하지않고 
가끔은 뒤를 돌아보면서 수정할 수 있는

'''