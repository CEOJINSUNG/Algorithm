# 파이썬으로 풀 수 있는 사람이 없었음 다 메모리 초과로 나옴

n = input()
m = input()

dp = [[0] * (len(n) + 2) for _ in range(len(m) + 2)]

for i in range(len(m) + 1):
    dp[i][0] = i
    dp[i][-1] = 2147000000
    
for j in range(len(n) + 1):
    dp[0][j] = j
    dp[-1][j] = 2147000000

dp[-1][-1] = 2147000000
for i in range(1, len(m) + 1):
    for j in range(1, len(n) + 1):
        if m[i-1] == n[j-1]:
            # 두 문자가 같은 경우, 추가 연산이 필요하지 않으므로 (i-1, j-1)에서 가져온다. 'c' 
            dp[i][j] = dp[i-1][j-1]
        else:
            # 두 문자가 다른 경우, (교체 'm'| 추가 'a' | 삭제 'd') 세 연산 중 cost가 가장 적은 것을 기록한다. 
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
len_n = len(n)
len_m = len(m)

i, j=0, 0
while True:
    minimum = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
    if dp[i+1][j+1] == minimum and dp[i][j] == dp[i+1][j+1]:
        print('c', m[i])
        i, j=i+1, j+1
    elif minimum == dp[i+1][j+1] and i != 0:
        print('m', m[i])
        i, j = i+1, j+1
    elif minimum == dp[i+1][j]:
        print('a', m[i])
        i, j = i+1, j
    elif minimum == dp[i][j+1]:
        i, j = i, j+1
    if i == len_m and j == len_n: break