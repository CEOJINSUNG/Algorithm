from collections import defaultdict
import sys
input = sys.stdin.readline

customer = int(input())
m, n = map(int, input().split())
a = [int(input()) for _ in range(m)]
b = [int(input()) for _ in range(n)]

a_pizza = defaultdict(int)
a_pizza[0] += 1
a_pizza[sum(a)] += 1
for i in range(m):
    temp = a[i]
    a_pizza[temp] += 1
    for j in range(1, m-1):
        temp += a[(i+j)%m]
        a_pizza[temp] += 1

b_pizza = defaultdict(int)
b_pizza[0] += 1
b_pizza[sum(b)] += 1
for i in range(n):
    temp = b[i]
    b_pizza[temp] += 1
    for j in range(1, n-1):
        temp += b[(i+j)%n]
        b_pizza[temp] += 1

answer = 0
for i in range(customer+1):
    answer += a_pizza[i] * b_pizza[customer - i]

print(answer)