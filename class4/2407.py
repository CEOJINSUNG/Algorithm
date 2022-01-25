N, M = map(int, input().split())

pascal = [[0] * (M+1) for _ in range(N+1)]

def combi(n, r):
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1
    else:
        if pascal[n][r] == 0:
            pascal[n][r] = combi(n-1, r) + combi(n-1, r-1)
        
        return pascal[n][r]

print(combi(N, M))