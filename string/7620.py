n = input()
m = input()

dp = [[0] * (len(n) + 1) for _ in range(len(m) + 1)]

for i in range(1, len(m) + 1):
    dp[i][0] = i
    
for j in range(1, len(n) + 1):
    dp[0][j] = j
    
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

trace_array = []

while len_n > -1 and len_m > -1:
    index_pos = min(dp[len_m-1][len_n], dp[len_m-1][len_n-1], dp[len_m][len_n-1])
    if index_pos == dp[len_m][len_n]:
        trace_array.append("c " + n[len_n-1])
        len_n -= 1
        len_m -= 1
    else:
        if index_pos == dp[len_m][len_n-1]:
            trace_array.append("d " + n[len_n-1])
            len_n -= 1
        elif index_pos == dp[len_m-1][len_n-1]:
            trace_array.append("m " + m[len_m-1])
            len_n -= 1
            len_m -= 1
        else:
            trace_array.append("a " + m[len_m-1])
            len_m -= 1

for index in range(len(trace_array)-2, -1, -1):
    print(trace_array[index])