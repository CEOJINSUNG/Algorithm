import math
from itertools import permutations

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    repeat = set()
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            num = "".join(num)
            if num[0] == "0":
                continue
            elif int(num) == 1:
                continue
            elif int(num) not in repeat:
                if is_prime_num(int(num)):
                    repeat.add(int(num))
                    answer += 1
    return answer