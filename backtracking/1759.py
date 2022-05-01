import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
security = list(map(str, sys.stdin.readline().split()))
security.sort()

# 모음
consonant = set(['a', 'e', 'i', 'o', 'u'])

# 조합
alphabet = combinations(security, l)

for i in alphabet:
    consonant_length = len(set(i)&consonant)
    if consonant_length > 0 and l-consonant_length > 1:
        print("".join(i))