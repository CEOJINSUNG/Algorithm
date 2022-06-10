from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = 0
    important = deque(list(map(int, input().split())))

    while important:
        best = max(important)
        front = important.popleft()
        m -= 1

        if best == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            important.append(front)
            if m < 0:
                m = len(important) - 1