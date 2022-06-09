n = int(input())
word = [input().strip() for i in range(n)]
word = list(set(word))

word.sort()
word.sort(key=lambda x: (len(x)))

for i in word:
    print(i)