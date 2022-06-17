from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        alpha, count = q.popleft()
        
        if alpha == target:
            answer = count
            break
        
        for word in words:
            differ = 0
            for i in range(len(alpha)):
                if differ > 1:
                    break
                if alpha[i] != word[i]:
                    differ += 1
            if differ == 1:
                q.append((word, count + 1))
    
    return answer