from collections import defaultdict
import sys
input = sys.stdin.readline

card = defaultdict(int)
n = int(input())
for _ in range(n):
    card[int(input())] += 1

print(sorted(card.items(), key = lambda x: (-x[1], x[0]))[0][0])