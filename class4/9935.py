import sys
input = sys.stdin.readline

word = input().strip()
boom = list(input().strip())
answer = []

for i in word:
    answer.append(i)
    if len(answer) >= len(boom) and answer[-len(boom):] == boom:
        del answer[-len(boom):]

print(*answer if answer else "FRULA",sep="")