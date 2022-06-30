import heapq

def solution(operations):
    answer = []
    minH, maxH = [], []
    
    for oper in operations:
        oper = oper.split()
        if oper[0] == "I":
            num = int(oper[1])
            heapq.heappush(maxH, ((-1)*num, num))
            heapq.heappush(minH, num)
        
        if oper[0] == "D":
            if oper[1] == "1" and len(maxH) != 0:
                num = heapq.heappop(maxH)[1]
                minH.remove(num)
            if oper[1] == "-1" and len(minH) != 0:
                num = heapq.heappop(minH)
                maxH.remove(((-1)*num, num))
    if minH:
        return [maxH[0][1], minH[0]]
    return [0, 0]