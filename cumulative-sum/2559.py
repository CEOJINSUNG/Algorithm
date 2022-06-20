n, k = map(int, input().split())
array = list(map(int, input().split()))

summary = [0]
temp = 0
for i in array:
    temp += i
    summary.append(temp)

answer = -int(1e9)
for start in range(n-k+1):
    use = summary[start+k] - summary[start]
    if use > answer:
        answer = use

print(answer)