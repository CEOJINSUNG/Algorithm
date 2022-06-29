from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
island = [[] for _ in range(n+1)]
animal = [["", 0] for _ in range(n+1)]
for i in range(2, n+1):
    t, a, p = map(str, input().split())
    island[int(p)].append(i)
    animal[i] = [t, int(a)]

def dfs(start):
    count = 0
    for i in island[start]:
        count += dfs(i)
    if animal[start][0] == "S" and start != 1:
        count += animal[start][1]
    elif animal[start][0] == "W":
        count = count - animal[start][1]
    if count < 0:
        count = 0
    return count

print(dfs(1))

# visited = [False]*(n+1)
# def bfs(start):
#     q = deque()
#     q.append((start, [start]))
#     visited[start] = True
#     result = []

#     while q:
#         exist = False
#         node, path = q.popleft()

#         for next in island[node]:
#             if not visited[next]:
#                 q.append((next, path + [next]))
#                 visited[next] = True
#                 exist = True
        
#         if not exist:
#             result.append(path)
#     return result

# answer = 0
# for route in bfs(1):
#     count = 0
#     for index in range(len(route)-1, 0, -1):
#         path = route[index]
#         cur_type, cur_count = animal[path]
#         if cur_count == 0:
#             continue
        
#         if cur_type == "W":
#             if count <= cur_count:
#                 count = 0
#             else:
#                 count -= cur_count
#         else:
#             count += cur_count
#             animal[path] = ["S", 0]
#     answer += count

# print(answer)