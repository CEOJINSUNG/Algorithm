import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A_sum = defaultdict(int)
B_sum = defaultdict(int)

for i in range(N):
    for j in range(i, N):
        A_sum[sum(A[i:j+1])] += 1

for i in range(M):
    for j in range(i, M):
        B_sum[sum(B[i:j+1])] += 1

answer = 0

for key in A_sum.keys():
    answer += B_sum[T - key] * A_sum[key]
print(answer)