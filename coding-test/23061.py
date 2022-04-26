import sys

n, m = map(int, sys.stdin.readline().split())

w = []
v = []

for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    w.append(weight)
    v.append(value)

knapsack = []
knapsack_weight = []
for _ in range(m):
    knapsack_weight.append(int(sys.stdin.readline()))

max_weight = max(knapsack_weight)

dp = [0 for _ in range(max_weight+1)]

for i in range(n):
    for j in range(max_weight, 0, -1):
        if j >= w[i]:
            dp[j] = max(dp[j-w[i]] + v[i], dp[j])

for i in range(m):
    knapsack.append(dp[knapsack_weight[i]]/float(knapsack_weight[i]))

weight = max(knapsack)
answer = knapsack.index(weight) + 1
print(answer)