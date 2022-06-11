s = input()

stack = []
answer = ""

temp = ""
ho = True
for i in range(len(s)-1, -1, -1):
    word = s[i]
    if word == ">":
        answer = temp + answer
        temp = ""
        ho = False
        temp = temp + word
    elif word == "<":
        ho = True
        temp = word + temp
        answer = temp + answer
        temp = ""
    else:
        if not ho:
            temp = word + temp
        else:
            if word == " ":
                answer = word + temp + answer
                temp = ""
            else:
                temp += word

if len(temp) > 0:
    answer = temp + answer

print(answer)