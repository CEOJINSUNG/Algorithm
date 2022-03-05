N = int(input())
A_List = list(map(int, input().split()))

answer = []

i, j = 0, 1

while i <= j:
    if i == N-1:
        break
    
    if A_List[i] != A_List[j]:
        answer += [j+1] * (j-i)
        i = j
        j += 1
    
    elif A_List[i] == A_List[j]:
        if j == N-1:
            answer += [-1] * (j-i)
            break

        else:
            j += 1

answer.append(-1)

print(*answer)