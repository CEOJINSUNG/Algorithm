string = input()

S = [0]
K = [0]

for i in range(len(string)):
    if string[i] == "S":
        S[i] += 1
    if string[i] == "K":
        K[i] += 1
    
    S += [S[i]]
    K += [K[i]]

del S[-1]
del K[-1]

length = [0]
max_size = 0

for s, k in zip(S, K):
    length[-1] += 1
    length += [length[-1]]

    if s == 2*k:
        max_size = length[-1]


print(length)
