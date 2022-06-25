from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
tree = []
target = []
area = []
for i in range(n):
    row = list(input().strip())
    for j in range(n):
        if row[j] == "B":
            tree.append((j, i))
        if row[j] == "E":
            target.append((j, i))
    area.append(row)

def status(position):
    row, col = True, True
    init = position[0]
    for i in range(3):
        if init[1] != position[i][1]:
            row = False
        if init[0] != position[i][0]:
            col = False
    
    if row:
        return "row"
    if col:
        return "col"

def up(position):
    for i in range(3):
        if position[i][1] - 1 < 0 or area[position[i][1]-1][position[i][0]] == "1":
            return [position, False]
    return [[(position[i][0], position[i][1]-1) for i in range(3)], True]

def down(position):
    for i in range(3):
        if position[i][1] + 1 >= n or area[position[i][1]+1][position[i][0]] == "1":
            return [position, False]
    return [[(position[i][0], position[i][1]+1) for i in range(3)], True]

def left(position):
    for i in range(3):
        if position[i][0] - 1 < 0 or area[position[i][1]][position[i][0]-1] == "1":
            return [position, False]
    return [[(position[i][0]-1, position[i][1]) for i in range(3)], True]

def right(position):
    for i in range(3):
        if position[i][0] + 1 >= n or area[position[i][1]][position[i][0]+1] == "1":
            return [position, False]
    return [[(position[i][0]+1, position[i][1]) for i in range(3)], True]

def rotate(position):
    if status(position) == "row":
        for i in range(3):
            row = position[i][0]
            col = position[i][1]
            if col-1 < 0 or col+1 >= n or area[col-1][row] == "1" or area[col+1][row] == "1":
                return [position, False]
        mid = sorted(position)[1]
        return [[(mid[0], mid[1]-1), (mid[0], mid[1]), (mid[0], mid[1]+1)], True]
    else:
        for i in range(3):
            row = position[i][0]
            col = position[i][1]
            if row-1 < 0 or row+1 >= n or area[col][row-1] == "1" or area[col][row+1] == "1":
                return [position, False]
        mid = sorted(position)[1]
        return [[(mid[0]-1, mid[1]), (mid[0], mid[1]), (mid[0]+1, mid[1])], True]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = []

tree.sort()
q = deque()
q.append((tree, 0))
visited.append(tree)

while q:
    node, num = q.popleft()

    if sorted(node) == sorted(target):
        print(num)
        exit()
    
    one = up(node)
    two = down(node)
    three = left(node)
    four = right(node)
    five = rotate(node)
    if one[1] and one[0] not in visited:
        visited.append(one[0])
        q.append((one[0], num+1))
    
    if two[1] and two[0] not in visited:
        visited.append(two[0])
        q.append((two[0], num+1))

    if three[1] and three[0] not in visited:
        visited.append(three[0])
        q.append((three[0], num+1))

    if four[1] and four[0] not in visited:
        visited.append(four[0])
        q.append((four[0], num+1))

    if five[1] and five[0] not in visited:
        visited.append(five[0])
        q.append((five[0], num+1))

print(0)