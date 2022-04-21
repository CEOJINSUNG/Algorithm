a = input()
b = input()

a_or_b = False
length = 0
if len(a) >= len(b):
    length = len(b)
    a_or_b = True
else:
    length = len(a)

a_list = []
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        temp = sorted(list(a[i:j]))
        if temp not in a_list:
            a_list.append(temp)

b_list = []
for i in range(len(b)):
    for j in range(i+1, len(b)+1):
        temp = sorted(list(b[i:j]))
        if temp not in b_list:
            b_list.append(temp)
answer = 0
for i in a_list:
    for j in b_list:
        if i == j:
            answer = max(answer, len(i))

print(answer)

# def compare(short, long):
#     global answer
#     short = sorted(list(short))
#     for i in range(len(long)):
#         for j in range(i+1, len(long)+1):
#             temp = sorted(list(long[i:j]))

#             if temp == short:
#                 answer = max(answer, len(temp))

# length = min(len(a), len(b))

# for left in range(length):
#     for right in range(left+1, length+1):
#         if a_or_b:
#             temp = b[left:right]
#             compare(temp, a)
#         else:
#             temp = a[left:right]
#             compare(temp, b)