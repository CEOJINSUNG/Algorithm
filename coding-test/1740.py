n = list(bin(int(input())))[2:]

answer = 0
for i in range(len(n) - 1, -1, -1):
    if n[i] == "1":
        answer += 3 ** (len(n) - 1 - i)

print(answer)