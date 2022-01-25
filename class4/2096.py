import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

max_temp = [0, 0, 0]
min_temp = [0, 0, 0]


for i in range(N):
    one, two, three = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_temp[j] = one + max(max_dp[j+1], max_dp[j])
            min_temp[j] = one + min(min_dp[j+1], min_dp[j])
        elif j == 1:
            max_temp[j] = two + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            min_temp[j] = two + min(min_dp[j-1], min_dp[j], min_dp[j+1])
        elif j == 2:
            max_temp[j] = three + max(max_dp[j], max_dp[j-1])
            min_temp[j] = three + min(min_dp[j], min_dp[j-1])
    
    for j in range(3):
        max_dp[j] = max_temp[j]
        min_dp[j] = min_temp[j]

print(max(max_dp), min(min_dp))