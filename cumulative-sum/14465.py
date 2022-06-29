import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
road = [0] + [1]*(n)
for _ in range(b):
    road[int(input())] = 0

for i in range(1, n+1):
    road[i] += road[i-1]

left, right = 0, k
answer = n
while left < right:
    if right == n+1:
        right -= 1
    
    mid = k - (road[right] - road[left]) 
    if mid < answer:
        answer = mid
    
    left += 1
    right += 1

print(answer)