class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return float("{0:.5f}".format(sum(salary[1:-1]) / len(salary[1:-1])))