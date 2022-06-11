n = int(input())
array = list(map(int, input().split()))

# 오큰수를 발견할 때 까지 넣는 스택
stack = [0]

# 정담 배열
answer = [-1] * n

for i in range(1, n):
    while stack and array[stack[-1]] < array[i]:
        answer[stack.pop()] = array[i]
    stack.append(i)

print(*answer)