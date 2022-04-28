from collections import defaultdict
import sys

name = sys.stdin.readline().strip()
length = len(name)

string = defaultdict(int)

for i in name:
    string[i] += 1

sorted_string = sorted(string.items(), key=lambda x: (-x[1], x[0]))
div = len(name) // 2
if length % 2 == 1:
    div += 1

result = ["" for _ in range(length)]
current = 0
odd = 0
while sorted_string:
    alphabet, number = sorted_string.pop(0)
    if odd > 1:
        break

    if number%2 == 1:
        number -= 1
        result[div-1] = alphabet
        odd += 1
    
    for _ in range(number//2):
        result[current] = alphabet
        result[length-current-1] = alphabet
        current += 1

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print("".join(result))