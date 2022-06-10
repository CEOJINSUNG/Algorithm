import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
compare = []
command = []
answer = []
current = 1

for num in array:
    while current <= n:
        if len(compare) > 0 and compare[-1] == num:
            command.append("-")
            answer.append(compare.pop())
            break

        if current <= num:
            command.append("+")
            compare.append(current)
        elif current == num:
            command.append("-")
            answer.append(compare.pop())
            break
        
        current += 1

while compare:
    answer.append(compare.pop())
    command.append("-")

if answer == array:
    for cmd in command:
        print(cmd)
else:
    print("NO")