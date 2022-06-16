import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

start = 0
end = k-1

belt = set()
while start < n:
    if end >= n:
        end -= n

    if end < start:
        setting = sushi[start:] + sushi[:end + 1]
    else:
        setting = sushi[start:end+1]
    
    current = set(setting)
    if c not in current:
        current.add(c)
    
    if len(belt) < len(current):
        belt = current
    
    start += 1
    end += 1

print(len(belt))