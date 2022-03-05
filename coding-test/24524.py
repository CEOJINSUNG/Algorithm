S = input()
T = input()

answer = [0] * len(T)

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            check = True
            for k in range(j):
                if answer[k] == 0 or answer[k] <= answer[j]:
                    check = False
