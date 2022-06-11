n = int(input())
top = list(map(int, input().split()))

answer = [0] * n
stack = []
for i in range(n):
    while stack:
        if top[i] > top[stack[-1]]:
            stack.pop()
        else:
            answer[i] = stack[-1] + 1
            break
    stack.append(i)

print(*answer)