# https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/
# https://towardsdatascience.com/solving-tsp-using-dynamic-programming-2c77da86610d
# from sys import maxsize
# from itertools import permutations

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp = [[0] * (1 << n-1) for _ in range(n)]

def dfs(x, visited):
    if dp[x][visited] != 0:
        return dp[x][visited]
    
    if visited == (1 << (n-1)) - 1:
        if graph[x][0]: 
            return graph[x][0]
        else:
            return INF

    min_route = INF
    for i in range(1, n):
        if not graph[x][i]:
            continue
        if visited & (1 << (i-1)):
            continue
        dist = dfs(i, visited | (1 << (i-1))) + graph[x][i]
        if dist < min_route:
            min_route = dist
    dp[x][visited] = min_route
    return min_route

print(dfs(0, 0))



# def DP_TSP(distances_array):
#   n = len(distances_array)
#   all_points_set = set(range(n))
  
#   # memo keys: tuple(sorted_points_in_path, last_point_in_path)
#   # memo values: tuple(cost_thus_far, next_to_last_point_in_path)
#   memo = {(tuple([i]), i): tuple([0, None]) for i in range(n)}
#   queue = [(tuple([i]), i) for i in range(n)]
  
#   while queue:
#     prev_visited, prev_last_point = queue.pop(0)
#     prev_dist, _ = memo[(prev_visited, prev_last_point)]
#     to_visit = all_points_set.difference(set(prev_visited))
    
#     for new_last_point in to_visit:
#       new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
#       new_dist = (prev_dist + distances_array[prev_last_point][new_last_point])
      
#       if (new_visited, new_last_point) not in memo:
#         memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
#         queue += [(new_visited, new_last_point)]
#       else:
#         if new_dist < memo[(new_visited, new_last_point)][0]:
#           memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
          
#   optimal_path, optimal_cost = retrace_optimal_path(memo, n)
#   return optimal_path, optimal_cost


# def retrace_optimal_path(memo, n):
#     points_to_retrace = tuple(range(n))
#     full_path_memo = dict((k, v) for k, v in memo.items() 
#                           if k[0] == points_to_retrace)
#     path_key = min(full_path_memo.keys(), key=lambda x: full_path_memo[x][0])
    
#     last_point = path_key[1]
#     optimal_cost, next_to_last_point = memo[path_key]
#     optimal_path = [last_point]
    
#     points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))
#     while next_to_last_point is not None:
#         last_point = next_to_last_point
#         path_key = (points_to_retrace, last_point)
#         _, next_to_last_point = memo[path_key]
        
#     optimal_path = [last_point] + optimal_path
#     return optimal_path, optimal_cost

# print(DP_TSP(graph))

# def travellingSalesmanProblem(graph, s):
#     vertex = [i for i in range(N) if i != s]
    
#     min_path = maxsize
#     next_permutation = permutations(vertex)
#     for i in next_permutation:
#         current_pathweight = 0
        
#         k = s
#         for j in i:
#             current_pathweight += graph[k][j]
#             k = j
#         current_pathweight += graph[k][s]

#         min_path = min(min_path, current_pathweight)
    
#     return min_path

# print(travellingSalesmanProblem(graph, s))