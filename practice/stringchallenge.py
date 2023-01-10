from collections import defaultdict

def string_challenge(str):
    start, length = 0, len(str)
    exist = False
    repeat = defaultdict(int)
    repeatMax = 1
    for i in range(length):
        char = str[i]
        if char == " ":
            start = i + 1
            repeat.clear()
        else:
            repeat[char] += 1
            if repeat[char] > repeatMax:
                exist = True
                repeatMax = repeat[char]
    
    for i in range(length):
        if exist:
            if str[i] == " ":
                return str[start:i]
            elif i == length - 1:
                return str[start:i+1]
    return -1

a = string_challenge("Hello apple pie")
b = string_challenge("No words")

print(a, b)