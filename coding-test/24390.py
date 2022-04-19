cooking = input().rstrip("\n")

m = int(cooking[0:2])
s = int(cooking[3:5])

total = m * 60 + s
count = 0
start = False

while True:
    if total < 10:
        if start == False:
            count += 1
            start = True
            break
        else:
            break

    if total >= 600:
        count += int(total/600)
        total %= 600
    
    elif total >= 60:
        count += int(total/60)
        total %= 60
    
    elif total >= 30:
        count += int(total/30)
        total %= 30
        start = True
    else:
        count += int(total/10)
        total %= 10

print(count)