# 연산자가 맞는지 확인하는 함수
def isOperator(op):
    return (op == '+' or op == '*' or op == '-')

# 최소 및 최댓값을 출력하는 함수
def printMinAndMaxValueOfExp(exp):
    num = []
    opr = []
    tmp = ""

    # 다른 벡터 방식으로 연산과 숫자를 저장함
    for i in range(len(exp)):
        if (isOperator(exp[i])):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp = ""
        else:
            tmp += exp[i]
    
    # 마지막 숫자를 저장
    num.append(int(tmp))

    llen = len(num)
    minVal = [[0 for i in range(llen)] for i in range(llen)]
    maxVal = [[0 for i in range(llen)] for i in range(llen)]

    # 2차원 배열 선언
    for i in range(llen):
        for j in range(llen):
            minVal[i][j] = 10**9
            maxVal[i][j] = 0

            if i == j:
                minVal[i][j] = maxVal[i][j] = num[i]
    
    # 연쇄 행렬 방법을 사용
    for L in range(2, llen + 1):
        for i in range(llen - L + 1):
            j = i + L - 1
            for k in range(i, j):
                minTmp = 0
                maxTmp = 0

                # 현재 연산자가 + 이면
                if opr[k] == '+':
                    minTmp = minVal[i][k] + minVal[k+1][j]
                    maxTmp = maxVal[i][k] + maxVal[k+1][j]
                
                elif opr[k] == '*':
                    minTmp = minVal[i][k] * minVal[k+1][j]
                    maxTmp = maxVal[i][k] * maxVal[k+1][j]
                
                elif opr[k] == '-':
                    minTmp = minVal[i][k] - minVal[k+1][j]
                    maxTmp = maxVal[i][k] - maxVal[k+1][j]

                if minTmp < minVal[i][j]:
                    minVal[i][j] = minTmp
                if maxTmp > maxVal[i][j]:
                    maxVal[i][j] = maxTmp
    
    print("최소 및 최대 값은 ", minVal[0][llen-1], maxVal[0][llen-1])

expression = "1*2+3*4*5-6*7*8*9*0"
printMinAndMaxValueOfExp(expression)