def combi(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    return combi(n-1) + combi(n-4)

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    if n <= 2: return 0
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    
    for p in range(2, n):
        if prime[p]:
            c += 1
    return c

def redJohn(n):
    return SieveOfEratosthenes(combi(n) + 1)