n, k = map(int, input().split())
num = input()
stack = []
temp = k

for i in range(n):
    while temp > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        temp -= 1
    stack.append(num[i])

print(''.join(stack[:n-k]))