n = int(input())

def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return False
    return True

def dfs(x):
    if len(str(x)) == n:
        print(x)
    else:
        for i in range(10):
            temp = x*10 + i
            if prime(temp):
                dfs(temp)

for i in [2, 3, 5, 7]:
    dfs(i)