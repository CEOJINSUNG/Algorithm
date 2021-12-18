n, k = map(int, input().split())

coin = []

DP = [0 for _ in range(k + 1)]

for i in range(n):
    coin.append(int(input()))

for i in range(1, k + 1):
    check = []
    # 각 코인을 순환
    for j in coin:
        # 코인을 순환하면서 불가능하지 않는 경우를 지속적으로 더해나감
        if j <= i and DP[i - j] != -1:
            check.append(DP[i - j])
    
    # 비어있으면 불가능하다는 의미
    if not check:
        DP[i] = -1
    # 비어 있지 않으면 최소 개수 + 1
    else:
        DP[i] = min(check) + 1

print(DP[k])