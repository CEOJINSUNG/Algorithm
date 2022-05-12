import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    applicant = []
    for _ in range(n):
        a, b = map(int, input().split())
        heapq.heappush(applicant, (a, b))
    
    answer = 1
    first, second = heapq.heappop(applicant)
    for _ in range(n-1):
        next_a, next_b = heapq.heappop(applicant)
        if next_b < second:
            second = next_b
            answer += 1
    
    print(answer)