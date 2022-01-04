N = int(input())
M = int(input())

repair = []
if M != 0:
    button = list(map(int, input().split()))
    repair.extend(button)

count = abs(N-100)
for i in range(1000001):
    jump = False
    for j in list(str(i)):
        if int(j) in repair:
            jump = True
            break
    if jump:
        continue
    else:
        count = min(count, abs(N-i) + len(str(i)))

print(count)