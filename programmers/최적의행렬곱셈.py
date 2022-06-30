def solution(matrix_sizes):
    dp = [[0 for j in range(len(matrix_sizes))] for i in range(len(matrix_sizes))]
    
    for gap in range(1, len(matrix_sizes)) : 
        for s in range(0, len(matrix_sizes)-gap) : 
            e = s+gap
            
            candidate = list()
            for m in range(s, e) :
                candidate.append(
                    dp[s][m]+dp[m+1][e]+
                    matrix_sizes[s][0]*matrix_sizes[m][1]*matrix_sizes[e][1])
            dp[s][e] = min(candidate)
            
    return dp[0][-1]