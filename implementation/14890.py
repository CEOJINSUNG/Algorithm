n, l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

count = 2*n

for row in board:
    for i in range(n-1):
        possible = True
        if abs(row[i+1]-row[i]) > 1:
            count -= 1
            break
        
        elif (row[i+1]-row[i] == 1) and (i - l + 1 < 0 or len(set(row[i-l+1:i+1])) != 1):
            possible = False
        
        elif (row[i]-row[i+1] == 1) and (i + l >= n or len(set(row[i+1:i+l+1])) != 1):
            possible = False

        if possible == False:
            count -= 1
            break

for j in range(n):
    for i in range(n-1):
        possible = True
        if abs(board[i+1][j]-board[i][j]) > 1:
            count -= 1
            break
        
        elif (board[i+1][j]-board[i][j] == 1):
            if i - l + 1 < 0:
                possible = False
            
            else:
                arr = []
                for k in range(i-l+1, i+1):
                    arr.append(board[k][j])
                
                if len(set(arr)) != 1:
                    possible = False

        
        elif (board[i][j]-board[i+1][j] == 1): 
            if i + l >= n:
                possible = False
            else:
                arr = []
                for k in range(i+1, i+l+1):
                    arr.append(board[k][j])
                
                if len(set(arr)) != 1:
                    possible = False

        if possible == False:
            count -= 1
            break

print(count)