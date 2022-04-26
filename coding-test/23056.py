import sys

n, m = map(int, sys.stdin.readline().split())

class_num = [0 for _ in range(n+1)]
class_student = [[] for _ in range(n+1)]

while True:
    num_name = input().split()
    num = int(num_name[0])
    name = num_name[1]

    if num == 0 and name == "0":
        break

    if class_num[num] < m:
        class_student[num].append([num, name])
        class_num[num] += 1

for i in range(1, n+1):
    if i%2 == 1:
        sorted_student = sorted(class_student[i], key=lambda x: (len(x[1]), x[1]))
        for j in sorted_student:
            print(*j)

for i in range(1, n+1):
    if i%2 == 0:
        sorted_student = sorted(class_student[i], key=lambda x: (len(x[1]), x[1]))
        for j in sorted_student:
            print(*j)