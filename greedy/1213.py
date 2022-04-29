from collections import defaultdict
import sys

d = defaultdict(int)
s = sys.stdin.readline().strip()

for i in s:
    d[i] += 1

center = ''
for key, value in d.items():
    if value%2 == 1:
        if len(center) > 0:
            print("I'm Sorry Hansoo")
            break
        center = key

else:
    ans = ''
    for key, value in sorted(d.items()):
        ans += key*(value//2)
    ans += center + ans[::-1]
    print(ans)