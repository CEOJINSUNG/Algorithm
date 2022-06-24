import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input().strip())
graph = [[] for _ in range(n+1)]
array = [0]
for i in range(1, n+1):
    num = int(input().strip())
    graph[num].append(i)

result = []
check = [0 for _ in range(n+1)]
def dfs(start, visited):
    visited.add(start)
    check[start] = 1

    for next in graph[start]:
        if next not in visited:
            dfs(next, visited.copy())
        else:
            result.extend(list(visited))

for i in range(1, n+1):
    if not check[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for x in result:
    print(x)