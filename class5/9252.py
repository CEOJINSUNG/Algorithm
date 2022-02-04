A = list(input())
B = list(input())

lcs = [[[0, ""] for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            lcs[i][j][0] = lcs[i-1][j-1][0] + 1
            lcs[i][j][1] = lcs[i-1][j-1][1] + A[i-1]
        else:
            if lcs[i][j-1][0] > lcs[i-1][j][0]:
                lcs[i][j][0] = lcs[i][j-1][0]
                lcs[i][j][1] = lcs[i][j-1][1]
            else:
                lcs[i][j][0] = lcs[i-1][j][0]
                lcs[i][j][1] = lcs[i-1][j][1]

print(lcs[len(A)][len(B)][0])
print(lcs[len(A)][len(B)][1])