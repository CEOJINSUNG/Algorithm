n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

info.sort()
for i in range(n):
    print(*info[i])