def longestCommonSubsequence(a, b, n, m):
    a = list(map(int, a.rstrip().split()))

    b = list(map(int, b.rstrip().split()))

    c = [[0] * (m+1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    
    lcs = []

    i, j = n, m
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs.append(a[i-1])
            i -= 1
            j -= 1
        else:
            if c[i-1][j] > c[i][j-1]:
                i -= 1
            else:
                j -= 1
    return reversed(lcs)