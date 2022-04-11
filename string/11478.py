string = input()

len_string = len(string)

array = set()

for i in range(len_string):
    for j in range(i, len_string):
        part = string[i:j+1]
        if part not in array:
            array.add(part)

print(len(array))