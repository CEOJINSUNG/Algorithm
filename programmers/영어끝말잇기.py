def solution(n, words):
    answer = [0, 0]
    already = []
    
    current, entire = 0, 1
    for word in words:
        current += 1
        if already:
            if already[-1][-1] != word[0]:
                answer = [current, entire]
                break
            elif word in already:
                answer = [current, entire]
                break
        already.append(word)
        
        if current == n:
            current = 0
            entire += 1

    return answer