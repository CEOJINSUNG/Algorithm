def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0]*m

    computeLPS(pat, lps)

    result = False
    i, j = 0, 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
        if j == m:
            result = True
            j = lps[j-1]
            break
    return result

def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

entire = input()
pattern = input()
if KMPSearch(pattern, entire):
    print(1)
else:
    print(0)