import sys
from bisect import bisect_left
input = sys.stdin.readline

while True:
    try:
        N = int(input())
        prices = list(map(int, input().split()))

        dp = [1]
        array = [prices[0]] 

        for i in range(1, N):
            idx = bisect_left(array, prices[i])
            if idx == len(dp):
                dp.append(dp[-1] + 1)
                array.append(prices[i]) 
            else: 
                array[idx] = prices[i]

        print(dp[-1])
    except:
        break