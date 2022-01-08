N, M = map(int, input().split())

listen = [input() for _ in range(N)]
watch = [input() for _ in range(M)]

people = set(listen) & set(watch)

print(len(people))
for i in sorted(people):
    print(i)