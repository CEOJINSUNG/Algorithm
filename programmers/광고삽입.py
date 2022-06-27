def transform(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def solution(play_time, adv_time, logs):
    play_time = transform(play_time)
    adv_time = transform(adv_time)               
    total_time = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = transform(start)
        end = transform(end)
        total_time[start] += 1
        total_time[end] -= 1

    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    most_view = 0
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < total_time[i] - total_time[i - adv_time]:
                most_view = total_time[i] - total_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time + 1

    return reverse(max_time)


def reverse(time):
    h = time // 3600
    time = time % 3600
    m = time // 60
    time = time % 60
    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s