import sys

n, m = map(int, sys.stdin.readline().split())

classroom = []
for _ in range(n):
    classroom.append(sorted(list(map(int, sys.stdin.readline().split()))))

# position은 현재 대표 선수들의 능력치를 가져온 값
position = [classroom[i][0] for i in range(n)]
max_value = max(position)
min_value = min(position)

# 여기서 index 는 학급을 의미하고 숫자는 각 학급 내 위치 순서
index_position = [0] * n
max_index = position.index(max_value)
min_index = position.index(min_value)


answer = max_value - min_value

while True:
    if index_position[min_index] >= m-1:
        print(answer)
        break

    # 최솟값을 가진 학급 내 위치가 변함
    index_position[min_index] += 1
    
    # 최솟값을 가진 학급 내 다음 선수가 들어옴
    position[min_index] = classroom[min_index][index_position[min_index]]

    # 능력치의 최고 값이랑 최솟 값 찾아서 갱신
    max_value = max(position)
    min_value = min(position)
    answer = min(answer, max_value - min_value)

    # 최댓값과 최솟값의 위치를 찾아줌
    max_index = position.index(max_value)
    min_index = position.index(min_value)