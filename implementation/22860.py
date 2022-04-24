from collections import defaultdict
import sys

folder_n, file_m = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(folder_n+file_m):
    p, f, c = map(str, sys.stdin.readline().split())
    graph[p].append((f, int(c)))

def bfs(query):
    query = query.split("/")
    q = [query[-1]]

    folder = []
    file = defaultdict(int)

    while q:
        current = q.pop(0)

        for value in graph[current]:
            if value[1] == 0:
                file[value[0]] += 1
            
            if value[1] == 1 and value[0] not in folder:
                folder.append(value[0])
                q.append(value[0])

    file_kind = 0
    file_total = 0
    for value in file.values():
        file_kind += 1
        file_total += value
    return [file_kind, file_total]

query_q = int(sys.stdin.readline())
for _ in range(query_q):
    query_q = sys.stdin.readline().rstrip("\n")
    print(*bfs(query_q))