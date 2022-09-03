import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

differ = a.difference(b)

if len(differ) > 0:
    print(len(differ))
    print(*sorted(differ))
else:
    print(0)
