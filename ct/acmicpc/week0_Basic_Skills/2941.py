check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
temp = []
cnt = 0

for i in check:
    if i in word:
        cnt += word.count(i)
        word = word.replace(i, " ")
for j in word:
    if j != " ":
        cnt += 1
print(cnt)

# commit test