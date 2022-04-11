from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

string = ""
distance = dict()

for _ in range(3):
    temp = input().strip()
    temp = temp.replace(" ", "")
    string += temp

string = int(string.replace("0", "9"))

def bfs():
    q = deque()
    q.append(string)
    distance[string] = 0

    while q:
        current = q.popleft()
        if current == 123456789:
            return distance[current]
        
        zero = str(current).find("9")
        x = zero//3 
        y = zero%3

        for i in range(4):
            new_x = x+dx[i] 
            new_y = y+dy[i]

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero = new_x * 3 + new_y
                new_s = list(str(current))
                new_s[zero], new_s[new_zero] = new_s[new_zero], new_s[zero]
                new_string = int("".join(new_s))
                
                if not distance.get(new_string):
                    distance[new_string] = distance[current] + 1
                    q.append(new_string)
    
    return -1

print(bfs())