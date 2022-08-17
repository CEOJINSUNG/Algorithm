from collections import deque
import sys, math
input = sys.stdin.readline

def is_prime(num):
    num = int(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited = set()
    visited.add(start)

    while q:
        number, count = q.popleft()

        if number == end:
            return count
        
        num = list(number)
        for i in range(4):
            target = num[i]
            if i == 0:
                for j in range(1, 10):
                    if j != int(target):
                        new_num = "".join([str(j)] + num[1:])
                        if is_prime(new_num) and new_num not in visited:
                            visited.add(new_num)
                            q.append((new_num, count + 1))
            else:
                for j in range(10):
                    if j != int(target):
                        new_num = "".join(num[:i] + [str(j)] + num[i+1:])
                        if is_prime(new_num) and new_num not in visited:
                            visited.add(new_num)
                            q.append((new_num, count + 1))
    return "impossible"

t = int(input())
for _ in range(t):
    a, b = map(str, input().split())
    print(bfs(a, b))