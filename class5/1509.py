import sys
input = sys.stdin.readline

question = input().rstrip()

dp = [[0 for _ in range(len(question) + 1)] for _ in range(len(question) + 1)]
answer = [float('inf')] * (len(question) + 1)
answer[0] = 0

for i in range(1, len(question) + 1):
    dp[i][i] = 1

for i in range(1, len(question)):
    if question[i-1] == question[i]:
        dp[i][i+1] = 1

for i in range(2, len(question)):
    for j in range(1, len(question)+1-i):
        if question[j-1] == question[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1, len(question) + 1):
    answer[i] = min(answer[i], answer[i-1]+1)
    for j in range(i+1, len(question)+1):
        if dp[i][j] != 0 :
            answer[j] = min(answer[j], answer[i-1] + 1)

print(answer[len(question)])