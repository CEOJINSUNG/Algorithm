n = int(input())
number = list(map(int, input().split()))

a, b = 0, 0
if len(number) > 2:
    if number[0] == number[1] :
        a = 0
    else:
        a = (number[1] - number[2]) // (number[0]-number[1])
    b = number[1] - a*number[0]
    answer = ""
    for i in range(1, n):
        num = int(number[i-1]*a + b)
        if num != number[i]:
            answer = "B"
            break
    if answer != "B": print(int(number[-1]*a + b))
    else: print(answer)
else:
    if len(number) < 2:
        print("A")
    else:
        if number[0] == number[1]:
            print(number[1])
        else:
            print("A")