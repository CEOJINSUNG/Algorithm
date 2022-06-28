n, x = map(int, input().split())

if (n-1)*(n-2) < 2*x:
    print(-1)
else:
    visited = [True]*(n+1)
    visited[n] = True
    visited[n-1] = True

    print(n, end=" ")

    mid = x
    temp = 0
    while mid >= 0:
        if (mid >= n - 1 - temp):
            print(temp, end=" ")
            mid -= (n - 1 - temp)
            visited[temp] = True
            temp += 1
        else:
            print(n - 1 - mid, end=" ")
            visited[n - 1 - mid] = True
            break
    print(n-1, end=" ")
    for i in range(n, 0, -1):
        if not visited[i]:
            print(i, end=" ")