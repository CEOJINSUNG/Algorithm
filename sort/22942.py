import sys
input = sys.stdin.readline

n = int(input())
circle = []
for num in range(n):
    x, d = map(int, input().split())
    circle.append((x-d, num))
    circle.append((x+d, num))

circle.sort()

stack = []
for i in range(n*2):
    d, c = circle[i]
    if len(stack) == 0:
        stack.append(circle[i])
    elif stack:
        if stack[-1][1] == c:
            stack.pop()
        else:
            stack.append(circle[i])

if stack:
    print("NO")
else:
    print("YES")