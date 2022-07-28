s = input()

one = list(s.split("0"))
two = list(s.split("1"))

one_list = 0
two_list = 0

for i in one:
    if (len(i) > 0):
        one_list += 1

for i in two:
    if (len(i) > 0):
        two_list += 1

print(min(one_list, two_list))