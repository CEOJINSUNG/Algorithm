n = int(input())

calender = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())

    for index in range(s, e+1):
        calender[index] += 1

x_len = 0
y_len = 0

answer = 0

for i in range(366):
    if calender[i] != 0:
        x_len = max(x_len, calender[i])
        y_len += 1
    else:
        answer += x_len * y_len
        x_len = 0
        y_len = 0


answer += x_len * y_len
print(answer)