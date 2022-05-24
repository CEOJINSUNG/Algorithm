from collections import deque
n = int(input())

parent = list(map(int, input().split()))
tree = [[[], 0, 0] for _ in range(n)]
visited = [False] * n

for i in range(1, n):
    tree[parent[i]][0].append(i)


answer = 0
if n == 1:
    print(1)
    exit(1)

paths = []
dfs_visited = [False] * n
def dfs():
    q = deque()
    q.append((0, [0]))
    dfs_visited[0] = True

    while q:
        current_node, current_path = q.pop()

        if len(tree[current_node][0]) == 0:
            paths.append(current_path)
            continue

        for next_node in tree[current_node][0]:
            if not dfs_visited[next_node]:
                q.append((next_node, [next_node] + current_path))
                dfs_visited[next_node] = True

dfs()

paths.sort(reverse=True)

visited[0] = True
for route in paths:
    # 마지막 노드를 방문했을 때는 넘긴다
    if visited[route[0]]:
        continue

    for i in range(len(route)-1, -1, -1):
        # 방문하지 않았을 때 부모의 사용횟수 + 1을 한다.
        if not visited[route[i]]:
            # 자신의 부모 노드
            parent_node = route[i+1]

            # 부모 노드의 사용횟수 갱신
            tree[parent_node][1] += 1

            # 자신까지 오는데 걸린 도달 시간 갱신 
            tree[route[i]][2] = tree[parent_node][1] + tree[parent_node][2]
            answer = max(answer, tree[route[i]][2])
            visited[route[i]] = True

print(answer)           