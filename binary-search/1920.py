n = int(input())
a = set(list(map(int, input().split())))

m = int(input())
verification = list(map(int, input().split()))

for veri in verification:
    if veri in a:
        print("1")
    else:
        print("0")