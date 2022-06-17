import sys
input = sys.stdin.readline

n = int(input())
friend = [input().rstrip() for _ in range(n)]
famous = [set() for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if (friend[i][k] == "Y" and friend[k][j] == "Y") or friend[i][j] == "Y":
                famous[j].add(i)
                famous[i].add(j)
answer = 0
for i in famous:
    if len(i) > answer:
        answer = len(i)
print(answer)