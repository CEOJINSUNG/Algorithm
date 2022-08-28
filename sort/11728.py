n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []
a_point, b_point = 0, 0

while a_point < n and b_point < m:
    if a[a_point] <= b[b_point]:
        result.append(a[a_point])
        a_point += 1
    else:
        result.append(b[b_point])
        b_point += 1

if a_point < n:
    result = result + a[a_point:]
else:
    result = result + b[b_point:]

print(*result)