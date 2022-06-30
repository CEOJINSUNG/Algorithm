from collections import deque

def find_coordinate(query, matrix):
    coordinate = []
    value = []
    x1, y1, x2, y2 = query
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    for y in range(y1, y2+1):
        coordinate.append((x1, y))
        value.append(matrix[x1][y])
    
    for x in range(x1+1, x2+1):
        coordinate.append((x, y2))
        value.append(matrix[x][y2])
    
    for y in range(y2-1, y1, -1):
        coordinate.append((x2, y))
        value.append(matrix[x2][y])
    
    for x in range(x2, x1, -1):
        coordinate.append((x, y1))
        value.append(matrix[x][y1])
    
    return coordinate, value
    
def solution(rows, columns, queries):
    answer = []
    matrix = [[i + columns*j for i in range(1, columns+1)] for j in range(rows)]
    
    for query in queries:
        coordinate, value = find_coordinate(query, matrix)
        value = deque(value)
        value.rotate(1)
        length = len(value)
        for index in range(length):
            x, y = coordinate[index]
            matrix[x][y] = value[index]
        answer.append(min(value))
    
    return answer