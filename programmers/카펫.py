def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, total+1):
        if total%i == 0:
            hori = total // i
            verti = i
            if hori < verti:
                break
            
            if (hori-2)*(verti-2) == yellow and 2*hori+2*(verti-2) == brown:
                answer = [hori, verti]
                break
    return answer