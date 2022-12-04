# 재귀적 풀이
def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n

# 반복적 풀이
def fibo(n):
    if n < 2:
        return n
    
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    
    return b

# 동적 계획법
def fibo(n):
    if n < 2:
        return n
    
    memo = [0 for _ in range(n+1)]
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]