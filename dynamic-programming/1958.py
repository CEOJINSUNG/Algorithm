one = input()
two = input()
three = input()

len_one = len(one)
len_two = len(two)
len_three = len(three)

dp = [[[0] * (len_three+1) for _ in range(len_two+1)] for _ in range(len_one+1)]

for i in range(1, len_one+1):
    for j in range(1, len_two+1):
        for k in range(1, len_three+1):
            if one[i-1] == two[j-1] and two[j-1] == three[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

answer = 0

for i in range(len_one+1):
    for j in range(len_two+1):
        answer = max(max(dp[i][j]), answer)

print(answer)