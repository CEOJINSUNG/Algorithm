def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

X = "WAHEWHEEEEE"
Y = "WHEEEEEEEEE"
m = len(X)
n = len(Y)
C = LCS(X, Y)

def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set()
        if C[i][j-1] >= C[i-1][j]:
            R.update(backTrackAll(C, X, Y, i, j-1))
        if C[i-1][j] >= C[i][j-1]:
            R.update(backTrackAll(C, X, Y, i-1, j))
        return R

for i in C:
    print(i)
print(backTrackAll(C, X, Y, m, n))

# n = int(input())
# given_s = input()

# dp = [[0 for _ in range(len(given_s) + 1)] for _ in range(len(given_s) + 1)]

# def findLCS(x, y, m, n):
#     s = []

#     if m == 0 or n == 0:
#         s.append("")
#         return s
    
#     if x[m-1] == y[n-1]:
#         tmp = findLCS(x, y, m-1, n-1)

#         for string in tmp:
#             s.append(string + x[m-1])
    
#     else:
#         if dp[m-1][n] >= dp[m][n-1]:
#             s = findLCS(x, y, m-1, n)
        
#         if dp[m][n-1] >= dp[m-1][n]:
#             tmp = findLCS(x, y, m, n-1)

#             for i in tmp:
#                 s.append(i)
    
#     return s

# def LCS(x, y, m, n):
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0 or j == 0:
#                 dp[i][j] = 0
#             elif x[i - 1] == y[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j],
#                               dp[i][j - 1])
#     return dp[m][n]

# LCS(given_s, 'WHEEEEEE', 8, 8)

# print(findLCS(given_s, 'WHEEEEEE', 8, 8))



# import sys
# sys.setrecursionlimit(100000000)

# def mainlcs(X, Y, m, n, lookup):
#     if m == 0 or n == 0:
#         return ['']

#     if X[m-1] == Y[n-1]:
#         lcs = mainlcs(X, Y, m-1, n-1, lookup)

#         for i in range(len(lcs)):
#             lcs[i] = lcs[i] + (X[m-1])
        
#         return lcs
    
#     if lookup[m-1][n] > lookup[m][n-1]:
#         return mainlcs(X, Y, m-1, n, lookup)
    
#     if lookup[m][n-1] > lookup[m-1][n]:
#         return mainlcs(X, Y, m, n-1, lookup)
    
#     top = mainlcs(X, Y, m-1, n, lookup)
#     left = mainlcs(X, Y, m, n-1, lookup)

#     return top + left


# def LCSLength(X, Y, lookup):
#     for i in range(1, len(X) + 1):
#         for j in range(1, len(Y) + 1):
#             if X[i-1] == Y[j-1]:
#                 lookup[i][j] = lookup[i-1][j-1] + 1
#             else:
#                 lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])

# def findLCS(X, Y):
#     lookup = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

#     LCSLength(X, Y, lookup)

#     lcs = mainlcs(X, Y, len(X), len(Y), lookup)

#     return lcs

# n = int(input())
# S = input()

# answer = 'WHEE'

# if n > 4:
#     for _ in range(n-4):
#         answer += 'E'

#     print(len(findLCS(S, 'WHEEEEE'))%1000000007)

# else:
#     print(0)