word = input()
ans = [0] * 35
for i in word:
    if ord(i) > 96:
        i = chr(ord(i) - 32)
    ans[ord(i)-65] += 1

if ans.count(max(ans)) > 1:
    print("?")
else:
    print(chr(ans.index(max(ans)) + 65))