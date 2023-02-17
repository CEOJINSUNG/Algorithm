class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # 물을 주며 움직일 때 어떤 전략을 사용하는 것이 더 나은가
        # 가까운 것부터 먼저 다 주고 난 다음
        # 만약 남은 물로 다음 식물에 완전히 물을 줄 수 있으면 넘어가서 물을 주고
        # 아니라면 다시 돌아와 물을 다 채우고 물을 줌
        answer = 0
        cur_capacity = capacity
        for i, plant in enumerate(plants):
            if cur_capacity < plant:
                answer += 2*i
                cur_capacity = capacity
            answer += 1
            cur_capacity -= plant
        return answer