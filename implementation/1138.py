n = int(input())

order = list(map(int, input().split()))

final = [0 for _ in range(n)]

for i in range(n):
    left = order[i]
    for j in range(n):
        if left == 0 and final[j] == 0:
            final[j] = i + 1
            break
        elif final[j] == 0:
            left -= 1

print(*final)