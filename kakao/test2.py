def solution(cost, x):
    # Write your code here
    n = len(cost)
    div = 10**9 + 7
    answer = 0
    money = 0
    for i in range(n-1, -1, -1):
        num = (2**i)%div
        if money + cost[i] > x:
            continue
        answer += num
        money += cost[i]
    return answer%div