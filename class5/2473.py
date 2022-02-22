N = int(input())
solution = sorted(list(map(int, input().split())))

answer = float('inf')
three_solution = []

for i in range(N-2):
    left, right = i+1, N-1
    mid = solution[i]

    while left < right:
        combi = solution[left] + solution[right] + mid

        if abs(combi) <= answer:
            three_solution = [mid, solution[left], solution[right]]
            answer = abs(combi)
        
        if combi >= 0:
            right -= 1
        
        elif combi < 0:
            left += 1

print(*three_solution)