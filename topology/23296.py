n = int(input())

floor = [0] + list(map(int, input().split()))
degree = [0] * (n+1)

for i in range(1, n+1):
    degree[floor[i]] += 1

# first floor is starting point
# so destination of index 1 should be the first queue
result = [floor[1]]
elevator = [1]
degree[floor[1]] -= 1
visited = [False] * (n+1)
visited[1] = True

# if everyone arrives in destination, degree should have only zero
while elevator:
    # find the next person and add the elevator
    next_person = floor[elevator.pop(0)]

    # go to the destination of next person
    result.append(floor[next_person])

    # if you did not visit a place
    if visited[next_person]:
        # find the place you didn't visit
        # if there is no where to go, break
        if len(set(degree)) == 1:
            break
        else:
            for i in range(1, n+1):
                if degree[i] != 0:
                    elevator.append(i)
                    break
        
    # if you did not visit a place, add next_person and decrease the degree
    else:
        visited[next_person] = True
        elevator.append(next_person)
        degree[floor[next_person]] -= 1

print(result)

