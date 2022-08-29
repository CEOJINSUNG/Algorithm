n, m = map(int, input().split())
invest = [[0]*(m+1)]

for _ in range(n):
    invest.append(list(map(int, input().split())))

profit = [[0]*(m+1) for _ in range(n+1)]
corporate = [[[0]*(m+1) for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        max_value = 0

        for k in range(i):
            if profit[k][j-1] + invest[i-k][j] > max_value:
                max_value = profit[k][j-1] + invest[i-k][j]
                max_pos = corporate[k][j-1][:]
                max_pos[j] = i-k

        if max_value > profit[i][j-1]:
            profit[i][j] = max_value
            corporate[i][j] = max_pos[:]
        else:
            profit[i][j] = profit[i][j-1]
            corporate[i][j] = corporate[i][j-1][:]

print(profit[n][m])
print(*corporate[n][m][1:])