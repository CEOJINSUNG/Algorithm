# 퇴사2
# 상담원으로 일하는 백준
# N + 1일째 퇴사
# a(n + 1) = max(a(n), a(n - t(n)) + p(n))

n = int(input())
working = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n):
    if i + working[i][0] <= n:
        dp[i + working[i][0]] = max(dp[i + working[i][0]], dp[i] + working[i][1])
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])