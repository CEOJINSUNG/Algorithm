n = input()
m = input()

def dist(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        dp[i][0] = i
    
    for j in range(1, len(str2) + 1):
        dp[0][j] = j
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                # 두 문자가 같은 경우, 추가 연산이 필요하지 않으므로 (i-1, j-1)에서 가져온다. 'c' 
                dp[i][j] = dp[i-1][j-1]
                print('c ' + str2[j-1])
            else:
                # 두 문자가 다른 경우, (교체 'm'| 추가 'a' | 삭제 'd') 세 연산 중 cost가 가장 적은 것을 기록한다. 
                m = dp[i-1][j-1]
                a = dp[i-1][j]
                d = dp[i][j-1]
                dp[i][j] = min(m, a, d) + 1
                
                if dp[i][j] == a+1:
                    print('a ', str1[i-1])
                elif dp[i][j] == m+1:
                    print('m '+ str1[i-1])
                elif dp[i][j] == d+1:
                    print('d ' + str1[i])

    
    return dp[-1][-1]

print(dist(n, m))