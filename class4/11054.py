import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp_increase = [1 for _ in range(N)]
dp_decrease = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

for i in range(N-1, -1, -1):
    for k in range(N-1, i, -1):
        if A[i] > A[k]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[k] + 1)

dp_total = [x+y-1 for x, y in zip(dp_increase, dp_decrease)]
print(max(dp_total))