from collections import defaultdict
import sys

n = int(sys.stdin.readline())
alphabet = defaultdict(int)
element = []

for _ in range(n):
    word = sys.stdin.readline().strip()

    element.append(word)
    length = len(word)

    for i in range(length):
        alphabet[word[i]] += 10**(length-1-i)

sorted_alphabet = sorted(alphabet.items(), key=lambda x: -x[1])
len_sorted = len(sorted_alphabet)

answer, current = 0, 9
for i in range(len_sorted):
    answer += sorted_alphabet[i][1]*(current-i)

print(answer)