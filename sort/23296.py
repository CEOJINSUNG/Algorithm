import heapq

# get values from input
n = int(input())
floor = [0] + list(map(int, input().split()))

# result means the elevator buttons 
result = []

# for get sequence, using degree
degree = [0] * (n+1)
for i in floor:
    degree[i] += 1

# for finding the person who did not use elevator, declare visited
visited = [True] + [False] * (n)

# using dfs, find the deepest path of tree
def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    result.append(floor[x])
    dfs(floor[x])

# starting point is first floor
dfs(1)

elevator = []

# by using heap, start the smallest value of degree
for i in range(1, n+1):
    if visited[i] == False:
        heapq.heappush(elevator, (degree[i], i))

while elevator:
    priority, current = heapq.heappop(elevator)

    if visited[current]: continue
    # if there is place elevator didn't visit, go to that place
    result.append(current)
    dfs(current)

# print the output
print(len(result))
print(*result)

# # if everyone arrives in destination, degree should have only zero
# while elevator:
#     if len(set(degree)) == 1 or len(set(visited)) == 1:
#         break
    
#     # get the current person and find next destination
#     current_person = elevator.pop(0)
#     visited[current_person] = True

#     # go to destination and add the visiting place
#     result.append(floor[current_person])
#     degree[floor[current_person]] -= 1

#     # find the next person
#     next_person = floor[current_person]

#     # if there is no person in that floor
#     if visited[next_person]:
#         # find the place you didn't visit
#         # if there is no where to go, break
#         for i in range(1, n+1):
#             if visited[i] == False:
#                 elevator.append(i)
#                 result.append(i)
#                 break
        
#         if len(set(degree)) == 1 or len(set(visited)) == 1:
#             break
#         # continue
#     # if you did not visit a place, add next_person and decrease the degree
#     else:
#         if len(set(visited)) != 1:
#             elevator.append(next_person)