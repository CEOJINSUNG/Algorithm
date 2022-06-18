from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split(' ')))
q = deque()
ans = []
for i in range(n):
    while q and q[-1][0] > arr[i]:
        q.pop()
    while q and q[0][1] < i - k + 1:
        q.popleft()
    q.append((arr[i],i))
    print(q[0][0], end = ' ')