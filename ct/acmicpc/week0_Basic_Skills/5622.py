data = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
word = input()
temp = 0

for i in word:
    temp += int(*[key for key, value in data.items() if i in value]) + 1

print(temp)
