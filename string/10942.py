import sys
input = sys.stdin.readline

# get size of array
n = int(input())

# get array
array = list(map(int, input().split()))

# dp
dp = [[0] * n for _ in range(n)]

for num_len in range(n):
    for start in range(n-num_len):
        end = start + num_len

        if start == end:
            dp[start][end] = 1
        elif array[start] == array[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

# get the number of questions
m = int(input())

# get each question
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])