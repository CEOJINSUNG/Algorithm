bar = list(input())
answer = 0
steel = []
for i in range(len(bar)):
    if bar[i] == "(":
        steel.append("(")
    else:
        if bar[i-1] == "(":
            steel.pop()
            answer += len(steel)
        else:
            steel.pop()
            answer += 1
print(answer)