from collections import deque, defaultdict

def solution(dirs):
    answer = 0
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    
    path = defaultdict(list)
    q = deque()
    q.append((0, 0))
        
    for dir in dirs:
        cur_x, cur_y = q.popleft()
        
        if dir == "U":
            new_x, new_y = cur_x + dx[0], cur_y + dy[0]
        elif dir == "D":
            new_x, new_y = cur_x + dx[1], cur_y + dy[1]
        elif dir == "L":
            new_x, new_y = cur_x + dx[2], cur_y + dy[2]
        elif dir == "R":
            new_x, new_y = cur_x + dx[3], cur_y + dy[3]
            
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            q.append((new_x, new_y))
            if (new_x, new_y) not in path[(cur_x, cur_y)] or (cur_x, cur_y) not in path[(new_x, new_y)]:
                path[(cur_x, cur_y)].append((new_x, new_y))
                path[(new_x, new_y)].append((cur_x, cur_y))
                answer += 1
        else:
            q.append((cur_x, cur_y))
    
    return answer