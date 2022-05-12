from collections import deque

a, b = map(int, input().split())

answer = 0

q = deque()
q.append((a, b, 1))

while q:
    current_a, current_b, current_count = q.popleft()

    if current_a == current_b:
        answer = current_count
        break

    elif current_a > current_b:
        answer = -1
        continue
    
    else:
        q.append((current_a*2, current_b, current_count+1))
        q.append((current_a*10+1, current_b, current_count+1))

print(answer)