import sys, heapq

t = int(sys.stdin.readline())

result = []

for _ in range(t):
    n = int(sys.stdin.readline())
    tree = list(map(int, sys.stdin.readline().split()))

    h = []
    for i in tree:
        heapq.heappush(h, (-i, i))

    if n >= 3:
        difference = 0
        center = heapq.heappop(h)[1]
        right = heapq.heappop(h)[1]
        left = heapq.heappop(h)[1]
        
        difference = max(difference, center-left)
        difference = max(difference, center-right)
        while h:
            if len(h) == 0:
                break

            if len(h) == 1:
                final = heapq.heappop(h)[1]
                difference = max(difference, right-final)
                break
            
            first = heapq.heappop(h)[1]
            second = heapq.heappop(h)[1]

            difference = max(difference, left-second)
            difference = max(difference, right-first)

            right, left = first, second

        result.append(difference)
    elif n == 2:
        result.append(abs(tree[0]-tree[1]))

    else:
        result.append(tree[0])

for i in result:
    print(i)