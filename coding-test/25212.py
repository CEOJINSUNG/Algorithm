from itertools import combinations

n = int(input())
piece = list(map(int, input().split()))

def calculate(array):
    total = 1
    for i in array:
        total *= i
    
    upper = 0
    for i in array:
        upper += (total/i)
    
    value = float(upper / total)
    if 0.99 <= value <= 1.01:
        return True
    else:
        return False

answer = 0
for i in range(1, n+1):
    for j in combinations(piece, i):
        if calculate(j):
            answer += 1
print(answer)