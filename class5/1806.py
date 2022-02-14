import sys
N, S = map(int, input().split())

array = list(map(int, input().split()))
left, right =0, 0
tmp_sum = 0
min_length = sys.maxsize

while True:
    if tmp_sum >= S:
        min_length = min(min_length, right-left)
        tmp_sum -= array[left]
        left += 1
    
    elif right == N:
        break
    else:
        tmp_sum += array[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)