import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    q1 = []
    q2 = []
    visited = [False]*k

    for i in range(k):
        command, num = input().split()

        if command == "I":
            heapq.heappush(q1, (int(num), i))
            heapq.heappush(q2, (-int(num), i))
            visited[i] = True
        else:
            if num == "1":
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)
    
    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)
    
    if not q1 or not q2:
        print("EMPTY")
    else:
        print("{0} {1}".format(-q2[0][0], q1[0][0]))