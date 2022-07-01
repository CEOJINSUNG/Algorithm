def solution(prices):
    length = len(prices)
    dp = [0]*length

    for i in range(length):
        for j in range(i+1, length):
            if prices[i] <= prices[j]:
                dp[i] += 1
            else:
                dp[i] += 1
                break
    return dp