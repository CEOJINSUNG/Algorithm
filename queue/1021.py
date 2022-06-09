from collections import deque, defaultdict

n, m = map(int, input().split())
queue = [i for i in range(1, n+1)]
position = list(map(int, input().split()))

index = defaultdict(int)
for num in position:
    index[num] = num-1

q = deque(queue)

def update_left():
    for key, value in index.items():
        if index[key] == 0:
            index[key] = len(q) - 1
        else:
            index[key] -= 1

def update_right():
    for key, value in index.items():
        if index[key] == len(q) - 1:
            index[key] = 0
        else:
            index[key] += 1

answer = 0
for num in position:
    while True:
        if q[0] == num:
            q.popleft()
            update_left()
            break
        else:
            if abs(len(q) - index[num]) > abs(index[num]):
                q.rotate(-1)
                answer += 1
                update_left()
            else:
                q.rotate(1)
                answer += 1
                update_right()

print(answer)