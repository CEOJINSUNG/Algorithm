N = int(input())

num = 0

while N >= 5:
    num += N // 5

    N //= 5

print(num)