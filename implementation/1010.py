def factorial(n):
    num = 1
    for i in range(n):
        num *= (i+1)
    return num

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n)*factorial(m-n)))