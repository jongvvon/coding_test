import sys
input = sys.stdin.readline

member = []
for case in range(int(input())):
    age, name = input().split()
    age = int(age)
    member.append([age, name])

sort_member = sorted(member, key=lambda x: x[0])

for age, name in sort_member:
    print(age, name)