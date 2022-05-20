import sys

test = int(sys.stdin.readline())
for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    book = [False] * (n+1)

    request = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        request.append([a, b])
    
    request.sort(key=lambda x: x[1])

    answer = 0
    while request:
        a, b = request.pop(0)

        for i in range(a, b+1):
            if not book[i]:
                answer += 1
                book[i] = True
                break
    
    print(answer)