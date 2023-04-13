from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * n
q = deque()

for i in range(n):
    while q and q[-1][1] > arr[i]:
        q.pop()
    
    while q and i - q[0][0] >= l:
        q.popleft()
    
    q.append((i, arr[i]))
    dp[i] = q[0][1]

print(*dp)
        