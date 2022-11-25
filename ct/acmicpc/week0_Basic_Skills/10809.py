alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = input()
for i in word:
    if i in alphabet:
        alphabet[alphabet.index(i)] = word.index(i)

for k in range(len(alphabet)):
    if type(alphabet[k]) == str:
        alphabet[k] = -1

print(*alphabet)
