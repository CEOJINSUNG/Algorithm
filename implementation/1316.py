import sys
input = sys.stdin.readline

answer = 0
n = int(input())
for _ in range(n):
    word = input().strip()
    check = [""]
    answer += 1
    for char in word:
        if check[-1] != char and char in check:
            answer -= 1
            break
        check.append(char)
print(answer)