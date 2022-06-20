n = int(input())
array = list(map(int, input().split()))

cumulative = [0]
temp = 0
for i in array:
    temp += i
    cumulative.append(temp)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(cumulative[b] - cumulative[a-1])