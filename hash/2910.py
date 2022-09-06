from collections import defaultdict
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
number = list(map(int, input().split()))

message = defaultdict(int)
for num in number:
    message[num] += 1

result = sorted(message.items(), key=lambda x: -x[1])
for item in result:
    for _ in range(item[1]):
        print(item[0], end=" ")
