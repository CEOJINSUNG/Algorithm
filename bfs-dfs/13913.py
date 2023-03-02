from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
path = [0] * 100001

q = deque()
q.append(n)

while q:
    node = q.popleft()

    if node == k:
        print(visited[node])
        ans = []
        while node != n:
            ans.append(node)
            node = path[node]
        ans.append(n)
        print(' '.join(map(str, ans[::-1])))
        break

    for next_node in (node - 1, node + 1, node * 2):
        if 0 <= next_node < 100001 and not visited[next_node]:
            visited[next_node] = visited[node] + 1
            q.append(next_node)
            path[next_node] = node