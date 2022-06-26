import sys
input = sys.stdin.readline

def dfs(index, count, learn, words):
    global result

    if count == k - 5:
        temp = 0
        for word in words:
            exist = True
            for char in word:
                if not learn[ord(char) - ord('a')]:
                    exist = False
                    break
            if exist:
                temp += 1
        result = max(temp, result)
        return
    
    for i in range(index, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, count+1, learn, words)
            learn[i] = False

n, k = map(int, input().split())
words = [set(input().strip()) for _ in range(n)]
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    learn = [0]*26
    result = 0

    for char in ["a", "c", "i", "n", "t"]:
        learn[ord(char) - ord('a')] = True
    
    dfs(0, 0, learn, words)
    print(result)