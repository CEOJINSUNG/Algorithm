class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        for num in digits:
            number += str(num)
        
        number = str(int(number) + 1)
        answer = []
        for num in number:
            answer.append(int(num))
        return answer