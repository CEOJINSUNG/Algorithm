def solution(n):
    ans = 0
    while n > 0:
        div = n%2
        n = n//2
        if div == 1: ans += 1
    return ans