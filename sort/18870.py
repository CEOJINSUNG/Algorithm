n = int(input())
x = list(map(int, input().split()))

sorted_x = sorted(set(x))
dic_x = {sorted_x[i]: i for i in range(len(sorted_x))}

for i in x:
    print(dic_x[i], end = ' ')