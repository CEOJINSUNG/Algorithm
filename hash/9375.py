t = int(input())

for _ in range(t):
    n = int(input())
    wear = {}

    for index in range(n):
        name, kind = map(str, input().split())
        if kind in wear:
            wear[kind].append(name)
        else:
            wear[kind] = [name]
    
    count = 1
    for key in wear:
        count *= (len(wear[key]) + 1)
    
    print(count - 1)