n = int(input())

binary = bin(n)
change = binary[2:]

len_binary = len(binary) - 2

for _ in range(32-len_binary):
    change = "0" + change

bosu = ""

for i in range(32):
    if change[i] == "0":
        bosu += "1"
    else:
        bosu += "0"

bosu = "0b" + bosu

bosu_ten = int(bosu, 2) + 1
bosu = bin(bosu_ten)

answer = 0

for a, b in zip(change, bosu[2:]):
    if a != b:
        answer += 1

print(answer)