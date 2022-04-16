n = int(input())

bus = []

for _ in range(n):
    s, e, c = map(int, input().split())
    
    bus.append((s, e, c))

bus.sort()

result = []
initial = bus[0]

for i in range(1, n):
    second = bus[i]

    if initial[1] >= second[0]:
        initial = (initial[0], max(initial[1], second[1]), min(initial[2], second[2]))
    else:
        result.append(initial)
        initial = second

if initial not in result:
    result.append(initial)
    
print(len(result))
for i in result:
    print(*i)