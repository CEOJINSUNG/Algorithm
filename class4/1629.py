import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(A, B):
    if B == 1:
        return A % C
    else:
        temp = power(A, B//2)
        if B % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * A % C

answer = power(A, B)
print(answer)
