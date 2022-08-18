n = int(input())

state = {}
answer = 0
for _ in range(n):
    city, code = map(str, input().split())
    city = city[:2]

    if city == code:
        continue
    
    if state.get((city, code)) == None:
        state[(city, code)] = 0
    state[(city, code)] += 1

    if state.get((code, city)) != None:
        answer += state[(code, city)]

print(answer)