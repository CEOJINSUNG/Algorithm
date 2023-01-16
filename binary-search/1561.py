n, m = map(int, input().split())
times = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()
left, right = 1, 10**20 * 30
standard = 0

while left <= right:
    mid = (left + right) // 2
    total = m + sum([mid // time for time in times])
    if total < n:
        left = mid + 1
    else:
        standard = mid
        right = mid - 1

cur = m + sum([(standard - 1) // time for time in times])

for i, time in enumerate(times):
    if standard % time == 0:
        cur += 1
    if cur == n:
        print(i+1)
        break