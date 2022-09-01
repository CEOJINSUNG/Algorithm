from collections import defaultdict
import sys
input = sys.stdin.readline

book = defaultdict(int)
n = int(input())
for _ in range(n):
    book[input().strip()] += 1

arr = sorted(book.items(), key = lambda x: (-x[1], x[0]))
print(arr[0][0])
