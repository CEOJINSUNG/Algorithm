from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 이벤트 시작날과 끝나는 날은 각 날을 포함하며 존재함
        # 어떤 날이든 해당 날에 참석할 수 있음 
        # 최대로 참석 가능한 회의장소 찾기
        # 가능한 날들을 집어 넣고 불가능한 날들은 빼는 방식으로 진행
        events.sort()
        heap = [] 
        count = 0
        i, n = 0, len(events)
        day = 0 
        
        while i < n or heap:
            if not heap:
                day = events[i][0]
            
            while i < n and day >= events[i][0]:
                heappush(heap, events[i][1])
                i += 1
            
            heappop(heap)
            count += 1
            day += 1

            while heap and heap[0] < day:
                heappop(heap)
        return count