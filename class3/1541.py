calculate = list(input())

answer = []
num = ""

while len(calculate) > 0:
    word = calculate.pop(0)
    if word == "+":
        answer.append(int(num))
        num = ""
    elif word == "-":
        answer.append(int(num))
        num = ""
        answer.append("-")
    else:
        num += word

answer.append(int(num))
ans = answer[0]
minus = False

if '-' not in answer:
    print(sum(answer))
else:
    for i in answer[1:]:
        if i == "-":
            minus = True
            continue

        if minus:
            ans -= i
        else:
            ans += i
    
    print(ans)
    

