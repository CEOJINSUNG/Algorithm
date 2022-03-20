S = list(input())
T = list(input())

answer = 0

while T:
    if len(S) > len(T):
        answer = 0
        break

    if S == T:
        answer = 1
        break

    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    
print(answer)