import sys

n, k = map(int, sys.stdin.readline().split())

# 3번째 시작 시간 및 분
hour = 21
minute = 0

# 3번째가 시작하는 날짜
current_day = 0

while current_day <= n:

    if minute >= 60:
        minute -= 60
        hour += 1
    
    if hour >= 24:
        hour -= 24
        current_day += 1
    
    if current_day >= n:
        break

    minute += k
    current_day += 1

    # print(hour, minute, current_day)

answer = []
if current_day > n:
    first = hour - 6
    second = hour - 3

    if first < 0:
        first += 24
    
    if second < 0:
        second += 24
    
    answer.append((first, minute))
    answer.append((second, minute))
elif current_day == n:
    first = hour - 6
    second = hour - 3
    third = hour + 18
    fourth = hour + 21

    if first >= 0: answer.append((first, minute))
    if second >= 0: answer.append((second, minute))
    answer.append((hour, minute))

    if len(answer) == 1:
        minute += k
        if minute >= 60:
            third += 1
            fourth += 1
            minute -= 60
        if third < 24: answer.append((third, minute))
        if fourth < 24: answer.append((fourth, minute))
    elif len(answer) == 2:
        minute += k
        if minute >= 60:
            third += 1
            minute -= 60
        if third < 24: answer.append((third, minute))

# print(hour, minute, current_day)

# if minute >= 60:
#     if hour + 1 == 24: hour = 0
#     else: hour += 1
#     minute -= 60

# if minute < 0:
#     if hour == 0: hour = 23
#     else: hour -= 1
#     minute += 60

# # print(hour, minute)
# times = [(hour-6, minute), (hour-3, minute), (hour, minute), (hour+18, minute+k), (hour+21, minute+k), (hour+24, minute+k)]

# for h, m in times:
#     if len(answer) >= 3:
#         continue

#     if h < 0 or h > 24:
#         continue
    
#     if m < 0:
#         answer.append((h-1, 60+m))

#     elif m >= 60:
#         if h + 1 < 24:
#             answer.append((h+1, m-60))
#         elif h + 1 == 24:
#             answer.append((0, m-60))
#     else:
#         if h < 24:
#             answer.append((h, m))
#         elif h == 24:
#             answer.append((0, m))

# print(times)
# print(over)

answer.sort()
print(len(answer))
for h, m in answer:
    print('{0:02d}:{1:02d}'.format(h, m))