from bisect import bisect_left
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    count = 0

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    for A in a:
        B = bisect_left(b, A)
        count += B
    print(count)