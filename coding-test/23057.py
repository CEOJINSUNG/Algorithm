import sys
from itertools import combinations

n = int(sys.stdin.readline())
# card = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

items = list(map(int, sys.stdin.readline().split()))
set_items = set(items)

for i in range(2, len(items) + 1):
    combi = list(combinations(items, i))
    for j in combi:
        sum_j = sum(j)
        if sum_j in set_items:
            continue
        else:
            set_items.add(sum_j)

total = sum(items)

print(total-len(set_items))

# def isPossible(x):
#     q = []
#     for i in card:
#         if x >= i:
#             q.append([i])
#             break
#     exist = False
#     while q:
#         current = q.pop(0)

#         sum_current = sum(current)

#         if sum_current == x:
#             # print(current)
#             exist = True
#             break

#         possible = [i for i in card if i < min(current)]

#         for k in possible:
#             if sum_current + k == x:
#                 exist = True
#                 break
#             elif sum_current + k < x:
#                 q.append(current+[k])
        
#         if exist:
#             # print(current)
#             break

#     if exist:
#         return True
#     else:
#         return False


# answer = 0 
# for i in range(1, total+1):
#     if isPossible(i):
#         answer += 1

# print(total-answer)