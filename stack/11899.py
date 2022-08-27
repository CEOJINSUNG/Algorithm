s = input().rstrip()
l = len(s)

while True:
    s = s.replace("()","")
    l -= 1
    
    if l == 0:
        print(len(s))
        break