from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])