n = int(input())
words = [input() for _ in range(n)]

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word) // 2])
        break