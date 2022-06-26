import sys
input = sys.stdin.readline

s = list("0"*21)
m = int(input())
for _ in range(m):
    command = input().strip().split()
    if command[0] == "add":
        x = int(command[1])
        s[x] = "1"
    elif command[0] == "remove":
        x = int(command[1])
        s[x] = "0"
    elif command[0] == "check":
        x = int(command[1])
        print(1 if s[x] == "1" else 0)
    elif command[0] == "toggle":
        x = int(command[1])
        if s[x] == "0": s[x] = "1"
        else: s[x] = "0"
    elif command[0] == "all":
        s = list("1"*21)
    elif command[0] == "empty":
        s = list("0"*21)