N = int(input())
board = [0] * 15
answer = 0

def check(a):
    for i in range(a):
        if abs(board[a] - board[i]) == abs(a - 1) or board[a] == board[i]:
            return False
    return True

def queen(a):
    global answer
    if a == N:
        answer += 1
        return
    else:
        for i in range(N):
            board[a] = i
            if check(a):
                queen(a+1)

queen(0)
print(answer)