def activity_selection(S, F, k, n, result):
    m = k + 1

    while m <= n and S[m] < F[k]:
        m = m + 1
    if m <= n:
        result.append('A' + str(m+1))
        return activity_selection(S, F, m, n, result)
    return None

result = ['A1']
S = [1, 2, 4, 1, 5, 8, 9, 11, 13]
F = [3, 5, 7, 8, 9, 10, 11, 14, 16]

activity_selection(S, F, 0, len(S)-1, result)   
print(result)