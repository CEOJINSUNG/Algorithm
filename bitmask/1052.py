n, k = map(int, input().split())

answer = 0
while bin(n).count('1') > k:
    plus = 2**(bin(n)[::-1].index('1'))
    answer += plus
    n += plus
print(answer)