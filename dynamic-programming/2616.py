cart_num = int(input())
customer = list(map(int, input().split()))
small_train_limit = int(input())

possible = [0]
value = 0

for i in customer:
    value += i
    possible.append(value)

dp = [[0] * (cart_num+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i*small_train_limit, cart_num+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], possible[j] - possible[j-small_train_limit])
        
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-small_train_limit] + possible[j] - possible[j-small_train_limit])

print(dp[3][cart_num])