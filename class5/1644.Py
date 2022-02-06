def prime(n):
    sieve = [True] * (n+1)
    
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    return [i for i in range(2, n+1) if sieve[i] == True]

N = int(input())

if N == 1:
    print(0)
else:
    prime_number = prime(N)
    sum = [0] * (len(prime_number) + 1)
    for i in range(len(prime_number)):
        sum[i+1] = sum[i] + prime_number[i]

    pt1, pt2 = 0, 1
    result = 0

    while (pt1 < len(sum)) and (prime_number[pt2-1] <= N):
        sub = sum[pt2] - sum[pt1]
        if sub == N:
            result += 1
            pt1 += 1
        elif sub > N:
            pt1 += 1
        else:
            if pt2 < len(sum) - 1:
                pt2 += 1
            else:
                pt1 += 1

    print(result)