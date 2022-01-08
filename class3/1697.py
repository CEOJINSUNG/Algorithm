N, K = map(int, input().split())

road = [0] * 100001

queue = [N]

while queue:
    node = queue.pop(0)

    if node == K:
        print(road[K])
        break

    for i in (node-1, node+1, node*2):
        if 0 <= i <= 100000 and not road[i]:
            road[i] = road[node] + 1
            queue.append(i) 