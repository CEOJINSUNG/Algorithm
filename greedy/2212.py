n = int(input())
k = int(input())
array = list(map(int, input().split()))
array.sort()

if k >= n:
    print(0)
else:
    dist = [array[i] - array[i-1] for i in range(1, n)]
    dist.sort(reverse=True)
    print(sum(dist[k-1:]))