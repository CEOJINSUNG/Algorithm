word = list(input())

for index in range(len(word)):
    if word[index] == 'B':
        word[index] = 'v'
    elif word[index] == 'E':
        word[index] = 'ye'
    elif word[index] == 'H':
        word[index] = 'n'
    elif word[index] == 'P':
        word[index] = 'r'
    elif word[index] == 'C':
        word[index] = 's'
    elif word[index] == 'Y':
        word[index] = 'u'
    elif word[index] == 'X':
        word[index] = 'h'
    else:
        word[index] = word[index].lower()

print("".join(word))