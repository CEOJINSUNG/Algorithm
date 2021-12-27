test_case = int(input())

def find_minimum_number(initial_x, initial_y, target_x, target_y, length):
    # 좌표선언
    matrix = [[False for _ in range(length)] for _ in range(length)]
    matrix[initial_x][initial_y] = True

    # 나이트가 움직이는 패턴
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    # 큐 선언
    q = []

    # 초기 값 삽입
    q.append((initial_x, initial_y, 0))

    while q:
        x_, y_, number = q.pop(0)

        if x_ == target_x and y_ == target_y:
            return number
        
        for i in range(8):
            new_x = x_ + dx[i]
            new_y = y_ + dy[i]

            if 0 <= new_x < length and 0 <= new_y < length and not matrix[new_x][new_y]:
                matrix[new_x][new_y] = True
                q.append((new_x, new_y, number + 1))

for _ in range(test_case):
    length = int(input())
    initial_x, initial_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    print(find_minimum_number(initial_x, initial_y, target_x, target_y, length))