N = int(input())
solution = list(map(int, input().split()))

answer = float('inf')
two_solution = []
left, right = 0, len(solution)-1

while left < right:
    combi = solution[left] + solution[right]

    if abs(combi) < answer:
        two_solution = [solution[left], solution[right]]
        answer = abs(combi)
    
    if combi >= 0:
        right -= 1
    
    elif combi < 0:
        left += 1

print(*two_solution)