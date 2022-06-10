n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2

    length = 0
    for one in tree:
        if one >= mid:
            length += (one - mid)
    
    if length >= m:
        start = mid + 1
    elif length < m:
        end = mid - 1

print(end)