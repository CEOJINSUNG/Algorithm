import sys
input = sys.stdin.readline

workers = set()
n = int(input())
for _ in range(n):
    person, type = map(str, input().split())
    if type == "enter":
        workers.add(person)
    else:
        workers.discard(person)

for worker in sorted(workers, reverse=True):
    print(worker)