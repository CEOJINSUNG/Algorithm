import sys

grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

temp = 0.0
total = 0.0
for _ in range(20):
    subject, time, alpha = map(str, sys.stdin.readline().split())
    if alpha == "P":
        continue

    total += (float(time) * grade[alpha])
    temp += (float(time))

print("{0:6f}".format(round(float(total/temp), 6)))