from collections import deque

n = int(input())
card = deque([i+1 for i in range(n)])
answer = []

count = 0
while card:
    if count%2 == 0:
        answer.append(card.popleft())
    else:
        card.rotate(-1)
    count += 1

print(answer[-1])