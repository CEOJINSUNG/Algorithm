import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = input().rstrip()

    left = []
    right = []
    cursor = 0
    for word in l:
        if word == ">":
            if right:
                left.append(right.pop())
        elif word == "<":
            if left:
                right.append(left.pop())
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word)
    
    print("".join(left) + "".join(reversed(right)))