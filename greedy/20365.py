n = int(input())
color = input()

blue, red = 0, 0

final = color[0]
if final == "R":
    red += 1
else:
    blue += 1

for i in range(1, n):
    if color[i] == "B":
        if final[-1] == "B":
            continue
        else:
            final += color[i]
            blue += 1
    else:
        if final[-1] == "R":
            continue
        else:
            final += color[i]
            red += 1

answer = 1
if blue >= red:
    answer += red
else:
    answer += blue

print(answer)


# 다른 사람 코드
import sys
input = sys.stdin.readline 

n = int(input())
p = input()
anw = p[0]

for i in p:
    if i != anw[-1]:
        anw += i

print(min(anw.count('B'), anw.count('R')) + 1)