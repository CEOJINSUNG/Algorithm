total =  int(input())
n = int(input())
for _ in range(n):
    price, amount = map(int, input().split())
    total -= price * amount

if total == 0:
    print("Yes")
else:
    print("No")